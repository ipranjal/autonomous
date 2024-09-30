#!/usr/bin/env python

import rospy
from crewai import Agent, Task, Crew
import llm
from campus.srv import NavigationRequest, NavigationRequestResponse
from crewai_tools import tool

from map import get_building_map


class BIAgent:
    def __init__(self,building):
        self.bi_agent_name = f"BI{building}"
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
        rospy.loginfo(f"BI Agent received request from {req.visitor_name} for host {req.host_name} in {req.building}")
        visitor = req.visitor_name
        host = req.host_name
        building = req.building

        task_send_navgation = Task(
            description="Provide internal navigation to {visitor} for {host} in {building}.",
            expected_output="Navigation path in format entrance->floor->office_no or Host you are trying to reach is not found in the building if host is not valid.",
            agent=self.bi_agent,
            tools=[self.provide_navigation],
            inputs={"visitor": visitor, "host": host, "building": building}
        )

        # task_go_oos = ConditionalTask(
        #     description=f"If visitor came to visit BI agent go out of service for 30 seconds.",
        #     expected_output="BI Agent is back in service after 30 seconds.",
        #     agent=self.bi_agent,
        #     condition= req.host_name == self.bi_agent_name,
        #     tools=[self.go_oos],
        #     inputs={"visitor":visitor, "host": host, "building": building}
        # )
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
        rospy.loginfo(f"BI Agent providing navigation for {visitor} to {host} in {building}.")
        building_map = get_building_map()
        building_map = building_map.get(building, {})
        path_in_building = building_map.get(host, "Invalid Host")
        #convert path in building to string path
        if path_in_building != "Invalid Host":
            navigation_path = " -> ".join(path_in_building)
        else :
            navigation_path = "Host you are trying to reach is not found in the building"
        return navigation_path
    
    @tool("go out of service for 30 seconds")
    def go_oos():
        """go out of service for 30 seconds"""
        rospy.loginfo(f"BI Agent  is going out-of-service (OOS) for 30 seconds.")  
        # Simulate OOS period
        rospy.sleep(30)
        rospy.loginfo(f"BI Agent is back in service.")
        return "BI Agent is back in service after 30 sec."

if __name__ == '__main__':
    rospy.init_node('bi_agent_node', anonymous=True)
    building = rospy.get_param('~building')
    bi_agent = BIAgent(building)
    bi_agent_name = f"BI{building}"

    rospy.loginfo(f"BI Agent {bi_agent_name} assigned to building: {building}")
    rospy.Service('navigation_service', NavigationRequest, bi_agent.handle_navigation_request)
    rospy.spin()