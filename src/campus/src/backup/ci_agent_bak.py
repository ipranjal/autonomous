#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from crewai import Agent, Task, Crew
from langchain_ollama import ChatOllama
import os
import map

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(
    model="llama3.1",
    base_url="http://localhost:11434"
)
bi_navigation_details = None

def update_position(publisher, x, y, z=0.0):
    pose_msg = PoseStamped()
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.header.frame_id = "map"  # Set the frame ID (e.g., map, odom)
    pose_msg.pose.position.x = x
    pose_msg.pose.position.y = y
    pose_msg.pose.position.z = z
    pose_msg.pose.orientation.w = 1.0
    publisher.publish(pose_msg)

def ci_agent_callback(data):
    visitor_name, host_name = data.data.split(',')
    
    # Determine the building based on the host's name
    building = "building_1" if "Host1" in host_name or "Host2" in host_name else "building_2"
    
    # Find path to the building
    path_to_building = map.find_shortest_path("campus_gate", building)
    
    # Publishers for CI agent and visitor positions
    ci_position_pub = rospy.Publisher('/ci_agent_position', PoseStamped, queue_size=10)
    visitor_position_pub = rospy.Publisher('/visitor_position', PoseStamped, queue_size=10)

    # Define the CI agent with CrewAI
    ci_agent = Agent(
        role="CI Agent",
        goal=f"Escort {visitor_name} to {building} and request BI agent for internal navigation.",
        backstory="A CI agent responsible for escorting visitors to the buildings.",
        llm=llm,
        verbose=True
    )
    
    # Create tasks
    task_navigate = Task(
        description=f"Guide {visitor_name} to {building}.",
        expected_output="Visitor is guided to the building.",
        agent=ci_agent,
        inputs={"visitor": visitor_name, "building": building}
    )
    
    task_request_bi = Task(
        description=f"Request floor navigation details for {building} from the BI agent.",
        expected_output="Internal navigation details received from BI agent.",
        agent=ci_agent,
        inputs={"visitor": visitor_name, "building": building}
    )
    
    my_crew = Crew(agents=[ci_agent], tasks=[task_navigate, task_request_bi])
    my_crew.kickoff(inputs={"visitor": visitor_name, "building": building})
    
    for waypoint in path_to_building:
        rospy.loginfo(f"Waypoint: {waypoint}")
        try:
            # Assuming each waypoint is a tuple (x, y)
            x, y = waypoint
            # Update the position of the CI agent
            pose_pub = ci_position_pub
            pose_msg = PoseStamped()
            pose_msg.header.stamp = rospy.Time.now()
            pose_msg.header.frame_id = "map"  # Set the frame ID (e.g., map, odom)
            pose_msg.pose.position.x = x
            pose_msg.pose.position.y = y
            pose_msg.pose.position.z = 0.0
            pose_msg.pose.orientation.w = 1.0
            pose_pub.publish(pose_msg)
            
            pose_pub = visitor_position_pub
            pose_msg = PoseStamped()
            pose_msg.header.stamp = rospy.Time.now()
            pose_msg.header.frame_id = "map"  # Set the frame ID (e.g., map, odom)
            pose_msg.pose.position.x = x
            pose_msg.pose.position.y = y
            pose_msg.pose.position.z = 0.0
            pose_msg.pose.orientation.w = 1.0
            pose_pub.publish(pose_msg)

            rospy.loginfo(f"CI Agent updated position to ({x}, {y})")
        except ValueError as e:
            rospy.logerr(f"Error unpacking waypoint {waypoint}: {e}")
        rospy.sleep(1)
    
    # Publish to BI agent for building navigation
    rospy.Publisher('bi_request', String, queue_size=10).publish(f"{visitor_name},{host_name},{building}")

def bi_agent_response_callback(data):
    global bi_navigation_details
    bi_navigation_details = data.data
    rospy.loginfo(f"Received navigation details from BI agent: {bi_navigation_details}")

def ci_agent_node():
    rospy.init_node('ci_agent_node', anonymous=True)
    rospy.loginfo(f"CI agent now available")
    rospy.Subscriber('visitor_info', String, ci_agent_callback)
    rospy.Subscriber('bi_navigation_details', String, bi_agent_response_callback)
    rospy.spin()

if __name__ == '__main__':
    ci_agent_node()
