import networkx as nx
import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
import random

campus_map = None
node_positions = None

# Define campus map as graph (nodes represent buildings and paths)
def create_campus_map():
    global campus_map
    campus_map = nx.Graph()
    campus_map.add_edge("campus_gate", "building_1", weight=10, mode="walk")
    campus_map.add_edge("campus_gate", "building_2", weight=15, mode="vehicle")
    campus_map.add_edge("building_1", "building_2", weight=5, mode="cycle")
    rospy.loginfo("Campus map created with nodes and edges.")

    return campus_map

# Building maps for internal navigation
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
    }
}


def assign_random_coordinates():
    global node_positions, campus_map
    if campus_map is None:
        rospy.logerr("The graph is not initialized.")
        return None
    node_positions = {}
    for node in campus_map.nodes:
       node_positions[node] = (random.uniform(0, 10), random.uniform(0, 10))  # Random 2D coordinates
    rospy.loginfo(f"Assigned random coordinates: {node_positions}")
    return node_positions

def find_shortest_path(start, end):
    global campus_map, node_positions
    if campus_map is None:
        rospy.logerr("campus map is not initialized.")
        return None
    
    if node_positions is None:
        rospy.logerr(" node_positions is not initialized.")
        return None
    
    # Find the shortest path in terms of nodes
    try:
        node_path = nx.shortest_path(campus_map, start, end, weight='weight')
    except nx.NetworkXNoPath:
        rospy.logerr(f"No path found between {start} and {end}.")
        return None
    
    # Convert node path to waypoints using node_positions
    waypoint_path = [node_positions[node] for node in node_path]
    
    return waypoint_path

def assign_random_host():
    return random.choice(["Host1", "Host2", "Host3", "Host4", "BIbuilding_1", "BIbuilding_2"])
