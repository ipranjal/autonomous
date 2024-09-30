#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from datetime import datetime
from peewee import *

# Define the SQLite database and penalty/pass log model
db = SqliteDatabase('/Users/pranjal/Desktop/autonomus-ai/penalty_log.db')

class EventLog(Model):
    timestamp = DateTimeField()
    agent_type = CharField()   # e.g., visitor_agent, ci_agent, bi_agent
    event_type = CharField()   # e.g., visitor_com_fail, visitor_com_pass
    status = CharField()       # pass or fail
    description = TextField(null=True)  # Optional description of the event

    class Meta:
        database = db

def log_event(agent_type, event_type, status, description=""):
    """Logs both pass and fail events in the database"""
    log = EventLog.create(
        timestamp=datetime.now(),
        agent_type=agent_type,
        event_type=event_type,
        status=status,
        description=description
    )
    log.save()

# Event callbacks for each agent
def visitor_event_callback(msg):
    rospy.loginfo(f"Visitor event: {msg.data}")
    event_type = msg.data
    if "pass" in event_type:
        log_event('visitor_agent', event_type, 'pass')
    else:
        log_event('visitor_agent', event_type, 'fail')

def ci_event_callback(msg):
    rospy.loginfo(f"CI event: {msg.data}")
    event_type = msg.data
    if "pass" in event_type:
        log_event('ci_agent', event_type, 'pass')
    else:
        log_event('ci_agent', event_type, 'fail')

def bi_event_callback(msg):
    rospy.loginfo(f"BI event: {msg.data}")
    event_type = msg.data
    if "pass" in event_type:
        log_event('bi_agent', event_type, 'pass')
    else:
        log_event('bi_agent', event_type, 'fail')

def institution_node():
    rospy.init_node('institution_node')
    rospy.loginfo("Attempting to connect to the database...")

    try:
        db.connect()
        db.create_tables([EventLog], safe=True)
        rospy.loginfo("Database connected and table created.")
    except Exception as e:
        rospy.logerr(f"Failed to connect to the database: {e}")

    # Subscribe to penalty events from different agents
    rospy.Subscriber('/visitor_agent/event', String, visitor_event_callback)
    rospy.Subscriber('/ci_agent/event', String, ci_event_callback)
    rospy.Subscriber('/bi_agent/event', String, bi_event_callback)

    rospy.spin()

if __name__ == "__main__":
    institution_node()
