#!/usr/bin/env python

import networkx as nx
import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
import map


def publish_map_graph():
    if map.node_positions is None:
        rospy.logerr("node_positions is not initialized.")
        return
    
    pub = rospy.Publisher('/campus_map', MarkerArray, queue_size=10)
    marker_array = MarkerArray()
   

    # Create markers for nodes (buildings)
    for idx, (node, pos) in enumerate(map.node_positions.items()):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "nodes"
        marker.id = idx  # Unique ID for each node
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        marker.pose.position.x = pos[0]
        marker.pose.position.y = pos[1]
        marker.pose.position.z = 0
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0
        marker_array.markers.append(marker)

        # Add text label for the building name
        text_marker = Marker()
        text_marker.header.frame_id = "map"
        text_marker.header.stamp = rospy.Time.now()
        text_marker.ns = "labels"
        text_marker.id = idx + 100  # Unique ID for the label
        text_marker.type = Marker.TEXT_VIEW_FACING
        text_marker.action = Marker.ADD
        text_marker.pose.position.x = pos[0]
        text_marker.pose.position.y = pos[1]
        text_marker.pose.position.z = 0.5  # Position the label above the sphere
        text_marker.scale.z = 0.3  # Font size
        text_marker.color.r = 1.0
        text_marker.color.g = 1.0
        text_marker.color.b = 1.0
        text_marker.color.a = 1.0
        text_marker.text = node  # Set the building name as text
        marker_array.markers.append(text_marker)

    # Create markers for edges (paths between buildings)
    for idx, (start_node, end_node) in enumerate(map.campus_map.edges):
        start_pos = map.node_positions[start_node]
        end_pos = map.node_positions[end_node]

        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "edges"
        marker.id = idx + 200  # Unique ID for each edge
        marker.type = Marker.LINE_STRIP
        marker.action = Marker.ADD
        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 0
        marker.scale.x = 0.05
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        # Define points for the line connecting the two nodes
        marker.points = [
            Point(start_pos[0], start_pos[1], 0),
            Point(end_pos[0], end_pos[1], 0)
        ]
        marker_array.markers.append(marker)

    pub.publish(marker_array)

if __name__ == '__main__':
    rospy.init_node('campus_map_publisher')

    map.create_campus_map()
    map.assign_random_coordinates()


    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        publish_map_graph()
        rate.sleep()