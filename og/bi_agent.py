import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from crewai import Agent, Task, Crew
from typing import Dict
from campus_map import building_maps
import os
from langchain_ollama import ChatOllama
import random

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(
    model="llama3.1",
    base_url="http://localhost:11434"
)

# Simulate OOS status
oos_status = False
oos_duration = 0

def bi_agent_callback(data):
    global oos_status, oos_duration
    
    visitor_name, host_name, building = data.data.split(',')
    
    if oos_status:
        rospy.loginfo(f"BI Agent is out of service and cannot assist {visitor_name} at the moment.")
        return
    
    # Check if visitor is meeting the BI agent itself
    if visitor_name == "BI_Agent":
        rospy.loginfo("BI Agent is meeting a visitor and is now OOS.")
        oos_status = True
        oos_duration = random.randint(5, 15)
        rospy.Timer(rospy.Duration(oos_duration), reset_oos_status, oneshot=True)
        return
    
    bi_agent = Agent(
        role="Building Incharge",
        goal=f"Provide navigation inside {building} for {visitor_name}",
        backstory="Responsible for navigating visitors inside the building.",
        llm=llm,
        verbose=True
    )
    
    # Get path inside building from the map
    path_in_building = building_maps[building].get(host_name, "Invalid Host")
    
    if path_in_building == "Invalid Host":
        rospy.loginfo(f"BI Agent: Host {host_name} not found in {building}")
        return
    
    task2 = Task(
        description=f"BI agent provides internal navigation for {visitor_name} to {host_name}",
        expected_output="Visitor reaches the host",
        agent=bi_agent,
        inputs={"visitor": visitor_name, "path": path_in_building}
    )
    
    my_crew = Crew(agents=[bi_agent], tasks=[task2])
    my_crew.kickoff(inputs={"visitor": visitor_name, "path": path_in_building})
    
    # Publish the agent's position
    pose_pub = rospy.Publisher('/bi_agent_position', PoseStamped, queue_size=10)
    pose_msg = PoseStamped()
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.header.frame_id = "map"
    pose_msg.pose.position.x = 10.0
    pose_msg.pose.position.y = 10.0
    pose_msg.pose.orientation.w = 1.0
    pose_pub.publish(pose_msg)
    
    rospy.loginfo(f"BI Agent provided navigation for {visitor_name}")

def reset_oos_status(event):
    global oos_status, oos_duration
    oos_status = False
    rospy.loginfo("BI Agent is back in service.")

def bi_agent_node():
    rospy.init_node('bi_agent_node', anonymous=True)
    rospy.Subscriber('bi_request', String, bi_agent_callback)
    rospy.spin()

if __name__ == '__main__':
    bi_agent_node()
