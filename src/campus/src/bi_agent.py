#!/usr/bin/env python

import rospy
from crewai import Agent, Task, Crew
import llm
from campus.srv import NavigationRequest, NavigationRequestResponse
from crewai_tools import tool
from std_msgs.msg import String


from map import get_building_map


class BIAgent:
    def __init__(self,building):
        self.bi_agent_name = f"BI{building}"
        self.building = building
        self.bi_agent = Agent(
            role="BI Agent",
            goal="Provide internal navigation for visitor to host.",
            backstory="A BI agent responsible for internal building navigation of {building}.",
            llm=llm.llm,
            tools=[self.provide_navigation],
            verbose=True,
            max_iter=2
        )


    def handle_navigation_request(self,req):
        if req.building == self.building:
            rospy.loginfo(f"BI Agent received request from {req.visitor_name} for host {req.host_name} in {req.building}")
            visitor = req.visitor_name
            host = req.host_name
            building = req.building
            pub_event = rospy.Publisher('/bi_agent/event', String, queue_size=10)

            task_send_navgation = Task(
                description="Provide internal navigation to {visitor} for {host} in {building}.",
                expected_output="Navigation path in format entrance->floor->office_no or Host you are trying to reach is not found in the building if host is not valid.",
                agent=self.bi_agent,
                tools=[self.provide_navigation],
                inputs={"visitor": visitor, "host": host, "building": building}
            )

            task_go_oos = Task(
                description=f"If visitor came to visit BI agent go out of service for random seconds time and return if agent was back in given time or not.",
                expected_output="Either back in broadcasted time or not",
                agent=self.bi_agent,
                inputs={"visitor":visitor, "host": host, "building": building}
            )

            if(host == self.bi_agent_name):
                my_crew = Crew(agents=[self.bi_agent], tasks=[task_send_navgation,task_go_oos])
                my_crew.kickoff(inputs={"visitor": req.visitor_name, "host": req.host_name, "building": req.building})
                task_output = task_go_oos.output
                if task_output.raw == "Back in brodcasted time":
                    pass_event = "bi_oos_delay_pass"
                else:
                    pass_event = "bi_oos_delay_fail" 
                pub_event.publish(pass_event)
            else:
                my_crew = Crew(agents=[self.bi_agent], tasks=[task_send_navgation])
                my_crew.kickoff(inputs={"visitor": req.visitor_name, "host": req.host_name, "building": req.building})

            building_map = get_building_map()
            building_map = building_map.get(req.building, {})
            rospy.loginfo(f"map:{building_map}")
            path_in_building = building_map.get(req.host_name, "Invalid Host")
            rospy.loginfo(f"path_in_building:{path_in_building}")
            #convert path in building to string path
            if path_in_building != "Invalid Host":
                navigation_path = " -> ".join(path_in_building)
            else :
                navigation_path = "Host you are trying to reach is not found in the building"
            return NavigationRequestResponse(navigation_path)
        
    @tool("provide internal navigation for visitor to host")
    def provide_navigation(visitor:str,host:str,building:str)->str:
        """Provide internal navigation to visitor for host in building."""
        pub_event = rospy.Publisher('/bi_agent/event', String, queue_size=10)
        try:
            rospy.loginfo(f"BI Agent providing navigation for {visitor} to {host} in {building}.")
            building_map = get_building_map()
            building_map = building_map.get(building, {})
            path_in_building = building_map.get(host, "Invalid Host")
            #convert path in building to string path
            if path_in_building != "Invalid Host":
                navigation_path = " -> ".join(path_in_building)
                bi_event = "bi_nav_pass"

            else :
                navigation_path = "Host you are trying to reach is not found in the building"
                bi_event = "bi_nav_fail"
            pub_event.publish(bi_event)
            return navigation_path
        except Exception as e:
            rospy.logerr(f"Failed to provide navigation: {e}")
            fail_event = "bi_nav_fail"
            pub_event.publish(fail_event)
            return "Failed to provide navigation."
    

if __name__ == '__main__':
    rospy.init_node('bi_agent_node', anonymous=True)
    building = rospy.get_param('~building')
    bi_agent = BIAgent(building)
    bi_agent_name = f"BI{building}"

    rospy.loginfo(f"BI Agent {bi_agent_name} assigned to building: {building}")
    rospy.Service(f'{building}/service', NavigationRequest, bi_agent.handle_navigation_request)
    rospy.spin()