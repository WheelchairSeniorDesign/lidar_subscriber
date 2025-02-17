#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/point_cloud2.hpp>  

class LidarLiveAnalyzer : public rclcpp::Node
{
public:
  LidarLiveAnalyzer()
  : Node("lidar_live_analyzer")
  {
    // Subscribe to /livox/lidar with a queue size of 10
    subscription_ = this->create_subscription<sensor_msgs::msg::PointCloud2>(
      "/livox/lidar",
      10,
      std::bind(&LidarLiveAnalyzer::lidarCallback, this, std::placeholders::_1)
    );

    RCLCPP_INFO(this->get_logger(), "C++ LidarLiveAnalyzer node started, listening on /livox/>
  }

private:
  void lidarCallback(const sensor_msgs::msg::PointCloud2::SharedPtr msg)
  {
    // Log the timestamp
    RCLCPP_INFO(
      this->get_logger(),
      "Received a Lidar message: %d s, %u ns",
      msg->header.stamp.sec,
      msg->header.stamp.nanosec
    );

    // TODO: Insert the live detection or real-time processing logic here.
  }

  rclcpp::Subscription<sensor_msgs::msg::PointCloud2>::SharedPtr subscription_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<LidarLiveAnalyzer>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}

