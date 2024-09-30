import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from crewai import Agent, Task, Crew
from typing import Dict
from langchain_ollama import ChatOllama
import os
from campus_map import find_shortest_path

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(
    model="llama3.1",
    base_url="http://localhost:11434"
)

# CI Agent handles navigation from campus entrance to the building
def ci_agent_callback(data):
    visitor_name, host_name = data.data.split(',')
    
    # CI agent logic
    ci_agent = Agent(
        role="Campus Incharge",
        goal="Escort visitor from campus entrance to the building.",
        backstory="Responsible for escorting visitors to their destination within the campus.",
        llm=llm,
        verbose=True
    )
    
    # CI agent guides the visitor to the building entrance
    campus_map = {
        "campus_gate": {"building_1": 10, "building_2": 15},  # Campus map representation
    }
    
    building = "building_1" if host_name == "Host1" else "building_2"  # Based on host
    
    path_to_building = find_shortest_path(campus_map, "campus_gate", building)
    
    task1 = Task(
        description=f"CI agent escorts {visitor_name} to {building}",
        expected_output="Visitor reaches the building entrance",
        agent=ci_agent,
        inputs={"visitor": visitor_name, "path": path_to_building}
    )
    
    my_crew = Crew(agents=[ci_agent], tasks=[task1])
    my_crew.kickoff(inputs={"visitor": visitor_name, "path": path_to_building})
    
    # Notify BI agent to get the internal navigation path
    rospy.Publisher('bi_request', String, queue_size=10).publish(f"{visitor_name},{host_name},{building}")
    
    # Publish the visitor's position
    pose_pub = rospy.Publisher('/ci_agent_position', PoseStamped, queue_size=10)
    pose_msg = PoseStamped()
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.header.frame_id = "map"
    pose_msg.pose.position.x = 5.0  # Example coordinates
    pose_msg.pose.position.y = 5.0
    pose_msg.pose.orientation.w = 1.0
    pose_pub.publish(pose_msg)
    
    rospy.loginfo(f"CI Agent {visitor_name} escorted to {building}")

def ci_agent_node():
    rospy.init_node('ci_agent_node', anonymous=True)
    rospy.Subscriber('visitor_info', String, ci_agent_callback)
    rospy.spin()

if __name__ == '__main__':
    ci_agent_node()
