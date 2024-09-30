#!/usr/bin/env python

import networkx as nx
import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
import random
from geometry_msgs.msg import PoseStamped


def create_campus_map():
        campus_map = nx.Graph()
        campus_map.add_edge("campus_gate", "building_1", weight=3, mode="walk")
        campus_map.add_edge("campus_gate", "building_2", weight=8, mode="walk")
        campus_map.add_edge("campus_gate", "building_3", weight=13, mode="vehicle")
        campus_map.add_edge("campus_gate", "building_3", weight=12, mode="cycle")
        campus_map.add_edge("campus_gate", "building_4", weight=18, mode="vehicle")
        campus_map.add_edge("building_1", "building_2", weight=5, mode="walk")
        campus_map.add_edge("building_1", "building_5", weight=9, mode="walk")
        campus_map.add_edge("building_2", "building_3", weight=10, mode="cycle")
        campus_map.add_edge("building_3", "building_4", weight=12, mode="vehical")
        campus_map.add_edge("building_4", "building_6", weight=10, mode="cycle")
        campus_map.add_edge("building_4", "building_6", weight=10, mode="walk")
        campus_map.add_edge("building_5", "building_7", weight=8, mode="walk")
        campus_map.add_edge("building_6", "building_7", weight=8, mode="walk")

        return campus_map
    
def create_building_maps():
        building_maps = {
            "building_1": {
                "Host1": ["entrance", "floor1", "office101"],
                "Host2": ["entrance", "floor2", "office201"],
                "BIbuilding_1": ["entrance", "floor0", "desk"]
            },
            "building_2": {
                "Host3": ["entrance", "floor1", "lab1"],
                "Host4": ["entrance", "floor3", "lab3"],
                "BIbuilding_2": ["entrance", "floor0", "desk"]
            },
            "building_3": {
                "Host5": ["entrance", "floor1", "office301"],
                "Host6": ["entrance", "floor2", "office302"],
                "BIbuilding_3": ["entrance", "floor0", "desk"]
            },
            "building_4": {
                "Host7": ["entrance", "floor1", "lab4"],
                "Host8": ["entrance", "floor2", "lab5"],
                "BIbuilding_4": ["entrance", "floor0", "desk"]
            },
            "building_5": {
                "Host9": ["entrance", "floor1", "conference101"],
                "Host10": ["entrance", "floor2", "office501"],
                "BIbuilding_5": ["entrance", "floor0", "desk"]
            },
            "building_6": {
                "Host11": ["entrance", "floor1", "office601"],
                "Host12": ["entrance", "floor2", "office602"],
                "BIbuilding_6": ["entrance", "floor0", "desk"]
            },
            "building_7": {
                "Host13": ["entrance", "floor1", "research_lab1"],
                "Host14": ["entrance", "floor2", "research_lab2"],
                "BIbuilding_7": ["entrance", "floor0", "desk"]
            }
        }
        return building_maps



campus_map = create_campus_map()
building_map = create_building_maps()
node_positions = {'building_1': (1.4648120118962753, 4.04156868739152), 'building_2': (1.8590013657999913, 1.6370616102292708), 'building_4': (6.726970062486378, 0.6775142244600305), 'building_3': (4.2652814229718015, 7.908774779817612), 'campus_gate': (0.6735613582113436, 3.499858299454438), 'building_5': (5.479361952381201, 2.103696429130733), 'building_6': (6.3212561570455845, 7.118723482188811), 'building_7': (3.362852783422399, 4)}

def get_campus_map():
    return campus_map

def get_node_positions():
    return node_positions

def get_building_map():
    return building_map

def find_shortest_path(start, end):
        map = get_campus_map()
        positions = get_node_positions()
        if map is None:
            print("campus map is not initialized.")
            return None
        
        if get_node_positions is None:
            print(" node_positions is not initialized.")
            return None
        
        # Find the shortest path in terms of nodes
        try:
            node_path = nx.shortest_path(map, start, end, weight='weight')
        except nx.NetworkXNoPath:
            print(f"No path found between {start} and {end}.")
            return None
        
        # Convert node path to waypoints using node_positions
        print(node_path)
        waypoint_path = [positions[node] for node in node_path]
        return waypoint_path



def init_ci_pos():
    positions = get_node_positions()
    ci_position_pub = rospy.Publisher(
            "/ci_agent_position", PoseStamped, queue_size=10
    )
    x,y = positions["campus_gate"]
    print(f"CI position: {x}, {y}")
    pose_pub = ci_position_pub
    pose_msg = PoseStamped()
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.header.frame_id = "map"  # Set the frame ID (e.g., map, odom)
    pose_msg.pose.position.x = x
    pose_msg.pose.position.y = y
    pose_msg.pose.position.z = 0.0
    pose_msg.pose.orientation.w = 0.0
    pose_pub.publish(pose_msg)    

def publish_map_graph():
    positions = get_node_positions()
    map = get_campus_map()
    if positions is None:
        print("node_positions is not initialized.")
        return
    
    pub = rospy.Publisher('/campus_map', MarkerArray, queue_size=10)
    marker_array = MarkerArray()
   

    # Create markers for nodes (buildings)
    for idx, (node, pos) in enumerate(positions.items()):
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
        marker.color.g = 0.1
        marker.color.b = 0.1
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
    for idx, (start_node, end_node) in enumerate(map.edges):
        start_pos = positions[start_node]
        end_pos = positions[end_node]

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
        marker.color.r = 0.2
        marker.color.g = 0.7
        marker.color.b = 0.2
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
    rospy.sleep(2)
    init_ci_pos()
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        publish_map_graph()
        rate.sleep()