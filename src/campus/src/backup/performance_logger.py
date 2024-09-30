import rospy

class PerformanceLogger:
    def __init__(self):
        self.ci_visitor_count = 0
        self.bi_navigation_count = 0
        self.violations = 0

    def log_ci_visitor(self):
        self.ci_visitor_count += 1
        rospy.loginfo(f"CI Agent has guided {self.ci_visitor_count} visitors")

    def log_bi_navigation(self):
        self.bi_navigation_count += 1
        rospy.loginfo(f"BI Agent has provided navigation {self.bi_navigation_count} times")

    def log_violation(self):
        self.violations += 1
        rospy.loginfo(f"Violation event occurred! Total violations: {self.violations}")
