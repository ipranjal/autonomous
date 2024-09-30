#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from crewai import Agent, Task, Crew
import llm
from crewai_tools import tool
from map import find_shortest_path
from campus.srv import NavigationRequest
from importlib import reload

class CIAgent:
    def __init__(self):
        self.ci_agent = Agent(
            role="CI Agent",
            goal=f"Escort visitors to building and request BI agent for internal navigation.",
            backstory="A CI agent responsible for escorting visitors to the buildings.",
            llm=llm.llm,
            verbose=True,
            max_iter=2,
        )
        self.init_pos()

    def init_pos(self):
        pose_pub = rospy.Publisher(
            "/ci_agent_position", PoseStamped, queue_size=10
        )
        x,y = (0.6735613582113436, 3.499858299454438)
        rospy.loginfo(f"CI Agent initial position setting up")
        pose_msg = PoseStamped()
        pose_msg.header.stamp = rospy.Time.now()
        pose_msg.header.frame_id = "map"  # Set the frame ID (e.g., map, odom)
        pose_msg.pose.position.x = x
        pose_msg.pose.position.y = y
        pose_msg.pose.position.z = 0.0
        pose_msg.pose.orientation.w = 0.0
        pose_pub.publish(pose_msg)

    def get_building_from_host(self, host):
        host_map = {
            "Host1": "building_1",
            "Host2": "building_1",
            "BIbuilding_1": "building_1",
            "Host3": "building_2",
            "Host4": "building_2",
            "BIbuilding_2": "building_2",
            "Host5": "building_3",
            "Host6": "building_3",
            "BIbuilding_3": "building_3",
            "Host7": "building_4",
            "Host8": "building_4",
            "BIbuilding_4": "building_4",
            "Host9": "building_5",
            "Host10": "building_5",
            "BIbuilding_5": "building_5",
            "Host11": "building_6",
            "Host12": "building_6",
            "BIbuilding_6": "building_6",
            "Host13": "building_7",
            "Host14": "building_7",
            "BIbuilding_7": "building_7"
        }
        return host_map.get(host, "Invalid Host")

    def ci_agent_callback(self, data):
        rospy.loginfo(f"CI Agent received request: {data.data}")
        visitor, host = data.data.split(",")
        building = self.get_building_from_host(host)
        
        rospy.loginfo(f"Visitor: {visitor}, Host: {host}, Building: {building}")

        task_navigate = Task(
            description="Guide {visitor} for meeting {host} to {building} by generating path from map.",
            expected_output="Visitor reached the building.",
            agent=self.ci_agent,
            tools=[self.generate_path_from_map],
            inputs={"visitor": visitor,"host": host, "building": building},
        )


        task_request_bi = Task(
            description="Request floor navigation details for {visitor} for meeting {host} in {building} from the BI agent.",
            expected_output="Internal navigation details from BI agent.",
            agent=self.ci_agent,
            tools=[self.request_bi_navigation_details],
            inputs={"visitor": visitor,"host": host, "building": building},
        )

        my_crew = Crew(agents=[self.ci_agent], tasks=[task_navigate, task_request_bi])
        my_crew.kickoff(inputs={"visitor": visitor, "host": host,"building": building})

        rospy.sleep(4)

        task_navigate_back = Task(
            description="Taking {visitor} back to campus gate from {building}",
            expected_output="Visitor reached back campus gate.",
            agent=self.ci_agent,
            inputs={"visitor": visitor, "building": building},
        )
        my_back_crew = Crew(agents=[self.ci_agent], tasks=[task_navigate_back])
        my_back_crew.kickoff(inputs={"visitor": visitor,"building": building})



    @tool("Generate path from map")
    def generate_path_from_map(visitor:str,host:str, building:str)->str:
        """Guide visitor for meeting host to building by generating path from map."""
        pub_event = rospy.Publisher('/ci_agent/event', String, queue_size=10)
        try:
            path_to_building = find_shortest_path("campus_gate", building)
            ci_position_pub = rospy.Publisher(
                "/ci_agent_position", PoseStamped, queue_size=10
            )
          
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
                    pose_msg.pose.orientation.w = 0.0
                    pose_pub.publish(pose_msg)

                 

                    rospy.loginfo(f"CI Agent updated position to ({x}, {y})")
                except ValueError as e:
                    rospy.logerr(f"Error unpacking waypoint {waypoint}: {e}")
                rospy.sleep(2)
            pass_event = "ci_navigation_pass"
            pub_event.publish(pass_event)
            return "Visitor reached the building."
        except Exception as e:
            rospy.logerr(f"Failed to generate path from map: {e}")
            fail_event = "ci_navigation_fail"
            pub_event.publish(fail_event)
            return "Failed to generate path from map."

    @tool("Request floor navigation from BI agent")
    def request_bi_navigation_details(visitor:str,host:str, building:str)->str:
        """Request floor navigation details from BI agent."""
        rospy.wait_for_service('navigation_service')
        pub_event = rospy.Publisher('/ci_agent/event', String, queue_size=10)
        try:
            # Create a service proxy to request navigation
            navigation_service = rospy.ServiceProxy('navigation_service', NavigationRequest)
            rospy.loginfo(f"Requesting BI navigation for visitor: {visitor}, host: {host}, building: {building}")

            # Make the request
            response = navigation_service(visitor, host, building)
            rospy.loginfo(f"CI Agent received navigation path: {response.navigation_path}")
            pass_event = "ci_com_pass"
            pub_event.publish(pass_event)
            return response.navigation_path
    
        except Exception as e:
            rospy.logerr(f"Service call failed: {e}")
            fail_event = "ci_com_fail"
            pub_event.publish(fail_event)
            return None


if __name__ == '__main__':
    rospy.init_node('ci_agent_node', anonymous=True)
    ci_agent = CIAgent()
    rospy.loginfo(f"CI agent now available")
    rospy.Subscriber('visitor_info', String, ci_agent.ci_agent_callback)
    rospy.spin()