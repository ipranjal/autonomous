#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from crewai import Agent, Task, Crew
import map
from langchain_ollama import ChatOllama
import os
import time

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(
    model="llama3.1",
    base_url="http://localhost:11434"
)

ci_guided_count = 0
oos_penalties = 0
oos_start_time = None
oos_duration = 300

# Define BI Agent logic
def bi_agent_callback(data):
    global ci_guided_count, oos_penalties, oos_start_time

    visitor_name, host_name, building = data.data.split(',')
    
    # Check if the request is for this BI agent's building
    if building != assigned_building:
        rospy.loginfo(f"BI Agent {bi_agent_name} received a request for {building}, but it is not assigned to this building.")
        return

    building_map = map.building_maps.get(building, {})

    # Define the BI agent with CrewAI
    bi_agent = Agent(
        role="BI Agent",
        goal=f"Provide internal navigation for {visitor_name} to {host_name}.",
        backstory="A BI agent responsible for internal building navigation.",
        llm=llm,
        verbose=True
    )

    # Publish the BI agent's location
    pose_pub = rospy.Publisher(f'/bi_agent_{building}_position', PoseStamped, queue_size=10)
    pose_msg = PoseStamped()
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.header.frame_id = "map"  # Set the frame ID (e.g., map, odom)
    pose_msg.pose.position.x = building_map.get('bi_agent_x', 0.0)
    pose_msg.pose.position.y = building_map.get('bi_agent_y', 0.0)
    pose_msg.pose.position.z = 0.0
    pose_msg.pose.orientation.w = 1.0
    pose_pub.publish(pose_msg)
    

    path_in_building = building_map.get(host_name, "Invalid Host")
    if path_in_building != "Invalid Host":
        task = Task(
            description=f"Guide {visitor_name} to {host_name} inside {building}.",
            expected_output="Visitor is guided to host.",
            agent=bi_agent,
            inputs={"visitor": visitor_name, "host": host_name}
        )
        my_crew = Crew(agents=[bi_agent], tasks=[task])
        my_crew.kickoff(inputs={"visitor": visitor_name, "host": host_name})
        rospy.loginfo(f"BI Agent {bi_agent_name} providing navigation for {visitor_name} to {host_name} via {path_in_building}")
        ci_guided_count += 1
        rospy.Publisher('bi_navigation_details', String, queue_size=10).publish(f"{visitor_name},{host_name},{path_in_building}")

    else:
        rospy.loginfo(f"BI Agent {bi_agent_name} could not find host {host_name} in {building}")

    if host_name == f"BI{building}":  # Special case: visitor wants to meet the BI agent itself
        if oos_start_time is None:
            oos_start_time = time.time()
        rospy.loginfo(f"BI Agent {bi_agent_name} is going out-of-service (OOS) for {oos_duration} seconds.")  
        # Publish OOS status
        rospy.Publisher('bi_oos_status', String, queue_size=10).publish(f"{visitor_name},{building},{oos_duration}")
        # Simulate OOS period
        time.sleep(oos_duration)
        oos_end_time = time.time()
        actual_oos_duration = oos_end_time - oos_start_time
        if actual_oos_duration > oos_duration:
            oos_penalties += 1
            rospy.logwarn(f"OOS penalty incurred. Total penalties: {oos_penalties}")
        oos_start_time = None
        
        # Resume service
        rospy.loginfo(f"BI Agent {bi_agent_name} is back in service.")
        return
    
   

def bi_agent_node():
    global assigned_building
    global bi_agent_name
    
    rospy.init_node('bi_agent_node', anonymous=True)
    
    # Get the building assignment from ROS parameters
    assigned_building = rospy.get_param('~building', 'default_building')
    bi_agent_name = f"BI{assigned_building}"
    
    rospy.loginfo(f"BI Agent {bi_agent_name} assigned to building: {assigned_building}")
    rospy.Subscriber('bi_request', String, bi_agent_callback)
    rospy.spin()

if __name__ == '__main__':
    bi_agent_node()
