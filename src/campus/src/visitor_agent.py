#!/usr/bin/env python

import llm
from crewai import Agent, Task, Crew
from crewai_tools import tool
import rospy
from std_msgs.msg import String
import random
import json

class VisitorAgent:
    def __init__(self, name, host):
        self.name = name
        self.host = host
        self.visitor_agent = Agent(
            role="Visitor",
            goal=f"Meet with {host} with help of Campus Incharge.",
            backstory="A visitor visit campus  and waits on campus entrance to be escorted to {host} by campus incharge.",
            llm=llm.llm,
            verbose=True,
            max_iter= 2
        )
        self.visit = Task(
            description="Visitor {visitor} talks to Campus Incharge campus at campus entrance to be escorted to {host}.",
            expected_output="Getting escorted to {host} by Campus Incharge.",
            agent=self.visitor_agent,
            inputs={"visitor": name, "host": host},
            tools=[self.talk_ci],
        )
        my_crew = Crew(agents=[self.visitor_agent], tasks=[self.visit])
        my_crew.kickoff(inputs={"visitor": self.name, "host": self.host})
        task_output = self.visit.output 
        


    @tool("Talk to campus incharge")
    def talk_ci(visitor: str, host: str) -> str:
        """Talk to campus incharge to be escorted to host."""
        rospy.loginfo(f"{visitor} talks to Campus Incharge to be escorted to {host}.")
        pub = rospy.Publisher("visitor_info", String, queue_size=10)
        rospy.sleep(1)  # Small delay to allow topic subscription
        pub.publish(f"{visitor},{host}")
        # Function logic here
        return f"Getting escorted to {host} by Campus Incharge."

def assign_random_host():
    return random.choice(["Host1", "Host2", "Host3", "Host4","Host5", "Host6", "Host7", "Host8","Host9", "Host10", "Host11", "Host12","Host13", "Host14", "BIbuilding_1", "BIbuilding_2","BIbuilding_3", "BIbuilding_4","BIbuilding_6", "BIbuilding_6","BIbuilding_7"])

if __name__ == '__main__':
    rospy.init_node('visitor_agent_node', anonymous=True)
    visitor_name = f"Visitor{random.randint(1, 100)}"
    host_name = assign_random_host()
    VisitorAgent(visitor_name, host_name)
