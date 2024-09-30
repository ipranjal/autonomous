#!/usr/bin/env python

import random
import rospy
from std_msgs.msg import String
from crewai import Agent, Task, Crew
import map
from langchain_ollama import ChatOllama
import os

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOllama(
    model="llama3.1",
    base_url="http://localhost:11434"
)

# Define Visitor Agent logic
def visitor_agent_node():
    rospy.init_node('visitor_agent_node', anonymous=True)
    pub = rospy.Publisher('visitor_info', String, queue_size=10)

    while not rospy.is_shutdown():
        visitor_name = f"Visitor{random.randint(1, 100)}"
        host_name = map.assign_random_host()
        
        # Define the Visitor agent with CrewAI
        visitor_agent = Agent(
            role="Visitor",
            goal=f"Meet with {host_name} with Campus Instructor.",
            backstory="A visitor is waiting for campus instructor trying to meet with a host on campus.",
            llm=llm,
            verbose=True
        )
        
        task = Task(
            description=f"Visitor {visitor_name} is waiting at the campus entrance to be escorted to {host_name}.",
            expected_output="Visitor is waiting to be escorted by campus instructor.",
            agent=visitor_agent,
            inputs={"visitor": visitor_name, "host": host_name}
        )
        
        my_crew = Crew(agents=[visitor_agent], tasks=[task])
        my_crew.kickoff(inputs={"visitor": visitor_name, "host": host_name})
        
        rospy.loginfo(f"Visitor {visitor_name} wants to meet {host_name}")
        pub.publish(f"{visitor_name},{host_name}")
        rospy.sleep(random.uniform(20, 500))  # Random interval between visitors

if __name__ == '__main__':
    visitor_agent_node()
