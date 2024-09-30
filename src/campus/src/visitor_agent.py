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
        self.visit_output = self.visit.output
        if "error" in self.visit_output.raw:
            pub_event = rospy.Publisher('/visitor_agent/event', String, queue_size=10)
            fail_event = "visitor_com_fail"
            pub_event.publish(fail_event)

        


    @tool("Talk to campus incharge")
    def talk_ci(visitor: str, host: str) -> str:
        """Talk to campus incharge to be escorted to host."""
        pub_event = rospy.Publisher('/visitor_agent/event', String, queue_size=10)
        try:
            rospy.loginfo(f"{visitor} talks to Campus Incharge to be escorted to {host}.")
            pub = rospy.Publisher("visitor_info", String, queue_size=10)
            rospy.sleep(1)  # Small delay to allow topic subscription
            pub.publish(f"{visitor},{host}")
            pass_event = "visitor_com_pass"
            pub_event.publish(pass_event)

            # Function logic here
            return f"Getting escorted to {host} by Campus Incharge."
        except Exception as e:
            rospy.logerr(f"Failed to talk to Campus Incharge: {e}")
            fail_event = "visitor_com_fail"
            pub_event.publish(fail_event)
            return "Failed to talk to Campus Incharge."

def assign_random_host():
    return random.choice(["Host1", "Host2", "Host3", "Host4","Host5", "Host6", "Host7", "Host8","Host9", "Host10", "Host11", "Host12","Host13", "Host14", "BIbuilding_1", "BIbuilding_2","BIbuilding_3", "BIbuilding_4","BIbuilding_6", "BIbuilding_6","BIbuilding_7"])

if __name__ == '__main__':
    rospy.init_node('visitor_agent_node', anonymous=True)
    visitor_count = 0
    while not rospy.is_shutdown():
        visitor_count += 1
        if visitor_count > 5:
            break
        # Create a random visitor with a random host
        visitor_name = f"Visitor{random.randint(1, 100)}"
        host_name = assign_random_host()
        VisitorAgent(visitor_name, host_name)

        # Introduce a random delay between 1 and 10 seconds before the next visitor arrives
        time_to_next_visitor = random.uniform(6, 10)
        rospy.sleep(time_to_next_visitor)
    # visitor_name = f"Visitor{random.randint(1, 100)}"
    # host_name = assign_random_host()
    # VisitorAgent(visitor_name, host_name)
