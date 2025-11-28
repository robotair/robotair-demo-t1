# import math

from rclpy.node import Node
from std_msgs.msg import String


class DemoPublisher(Node):
    """Provides a simple publisher for ROS2 Nodes to send messages"""

    sum = 1
    count = 1

    def __init__(self):
        """Create the Node Publisher and set an initial timer
        """
        super().__init__("robotair_demo_publisher")
        self.publisher_ = self.create_publisher(String, "demo_topic", 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        """Callback for the timer function to print the message"""
        msg = String()
        msg.data = f"The total sum is {self.sum} after {self.count} counts"
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing message")
        self.count += 1
        self.sum += self.count
        # self.sum += math.sqrt(self.count)
