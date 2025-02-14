#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2

class LivoxDataSaver(Node):
    def __init__(self):
        super().__init__('livox_data_saver')
        self.subscription = self.create_subscription(
            PointCloud2,            # or custom Livox type
            '/livox/lidar',
            self.lidar_callback,
            10
        )
        self.log_file_path = '/tmp/livox_data.log'
        self.get_logger().info(f"Saving Livox data to {self.log_file_path}")

    def lidar_callback(self, msg):
        # Convert msg to string (or parse as needed) and append to file
        with open(self.log_file_path, 'a') as f:
            f.write(str(msg) + "\n")

def main(args=None):
    rclpy.init(args=args)
    node = LivoxDataSaver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
