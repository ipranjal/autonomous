#!/usr/bin/env python

import peewee
from peewee import *
from prettytable import PrettyTable

# Define the SQLite database
db = SqliteDatabase('/Users/pranjal/Desktop/autonomus-ai/penalty_log.db')

# EventLog Model (assuming it has already been defined)
class EventLog(Model):
    timestamp = DateTimeField()
    agent_type = CharField()   # e.g., visitor_agent, ci_agent, bi_agent
    event_type = CharField()   # e.g., visitor_com_fail, ci_navigation_pass
    status = CharField()       # pass or fail
    description = TextField(null=True)

    class Meta:
        database = db

def calculate_performance(pass_count, fail_count):
    total = pass_count + fail_count
    if total == 0:
        return 0  # Avoid division by zero
    return (pass_count / total) * 100

def generate_performance_matrix():
    db.connect()

    # Query to count pass, fail, and total events for each agent type
    agents = ['visitor_agent', 'ci_agent', 'bi_agent']
    performance_table = PrettyTable()
    performance_table.field_names = ["Agent", "Pass Events", "Fail Events", "Total Events", "Penalties", "Performance (%)"]

    for agent in agents:
        # Count pass and fail events for each agent
        pass_count = EventLog.select().where((EventLog.agent_type == agent) & (EventLog.status == 'pass')).count()
        fail_count = EventLog.select().where((EventLog.agent_type == agent) & (EventLog.status == 'fail')).count()
        total_count = pass_count + fail_count
        
        # Performance Percentage
        performance_percentage = calculate_performance(pass_count, fail_count)
        
        # Get specific penalty event counts
        penalty_events = EventLog.select(EventLog.event_type, peewee.fn.COUNT(EventLog.event_type).alias('count')) \
                                .where((EventLog.agent_type == agent) & (EventLog.status == 'fail')) \
                                .group_by(EventLog.event_type)
        
        penalty_summary = ', '.join([f"{event.event_type}: {event.count}" for event in penalty_events])
        
        # If there are no penalties, show a default message
        if not penalty_summary:
            penalty_summary = "No penalties"
        
        # Add the row to the table
        performance_table.add_row([agent, pass_count, fail_count, total_count, penalty_summary, round(performance_percentage, 2)])

    # Display the performance table
    print(performance_table)
    
    db.close()

if __name__ == "__main__":
    generate_performance_matrix()
