#!/usr/bin/env python

import rospy
from campus.srv import NavigationRequest, NavigationRequestResponse

def handle_service_request(req):
    # Determine which bi_agent node should handle the request based on the condition
    service_name = f"{req.building}/service"
    rospy.loginfo(f"Requesting service from {service_name}")
    
    rospy.wait_for_service(service_name)
    try:
        bi_agent_service = rospy.ServiceProxy(service_name, NavigationRequest)
        response = bi_agent_service(req)
        return response
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return None

def dispatcher():
    rospy.init_node('service_request_dispatcher')
    rospy.Service('navigation_service', NavigationRequest, handle_service_request)
    rospy.spin()

if __name__ == "__main__":
    dispatcher()
