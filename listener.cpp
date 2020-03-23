#include "ros/ros.h"
#include "std_msgs/String.h"
void welcome_messageCallback(const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO("[%s]", msg->data.c_str());
}
int main(int argc, char **argv)
{
    ros::init(argc, argv, "listener");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("welcome_message", 1000, welcome_messageCallback);
    ros::spin();
    return 0;
}