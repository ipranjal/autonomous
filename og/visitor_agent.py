import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from crewai import Agent, Task, Crew
from typing import Dict
from langchain_ollama import ChatOllama
import os

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(
    model="llama3.1",
    base_url="http://localhost:11434"
)

# Visitor waits to be escorted
def visitor_agent_callback(data):
    visitor_name, host_name = data.data.split(',')
    
    visitor_agent = Agent(
        role="Visitor",
        goal=f"Meet with {host_name}",
        backstory="A visitor coming to the campus.",
        llm=llm,
        verbose=True
    )
    
    task3 = Task(
        description=f"Visitor agent waits to be escorted to meet {host_name}",
        expected_output="Visitor is waiting at the campus gate",
        agent=visitor_agent,
        inputs={"visitor": visitor_name}
    )
    
    my_crew = Crew(agents=[visitor_agent], tasks=[task3])
    my_crew.kickoff(inputs={"visitor": visitor_name})
    
    # Publish position
    pose_pub = rospy.Publisher('/visitor_agent_position', PoseStamped, queue_size=10)
    pose_msg = PoseStamped()
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.header.frame_id = "map"
    pose_msg.pose.position.x = 2.0
    pose_msg.pose.position.y = 2.0
    pose_msg.pose.orientation.w = 1.0
    pose_pub.publish(pose_msg)

    rospy.loginfo(f"Visitor {visitor_name} is waiting to meet {host_name}")

def visitor_agent_node():
    rospy.init_node('visitor_agent_node', anonymous=True)
    rospy.Subscriber('visitor_info', String, visitor_agent_callback)
    rospy.spin()

if __name__ == '__main__':
    visitor_agent_node()
