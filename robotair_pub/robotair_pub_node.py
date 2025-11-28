import rclpy
from robotair_pub import robotair_publisher


def main(args=None):
    """Main method to be called as entry point for the publisher"""
    rclpy.init(args=args)
    _demo_publisher = robotair_publisher.DemoPublisher()
    rclpy.spin(_demo_publisher)
    _demo_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
