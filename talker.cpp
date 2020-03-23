#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "talker");
    ros::NodeHandle n;
    ros::Publisher welcome_message_pub = n.advertise<std_msgs::String>("welcome_message", 1000);
    ros::Rate loop_rate(10);
    while (ros::ok())
    {
        std_msgs::String msg;
        std::stringstream ss;
        ss << "Welcome to Abhiyaan";
        msg.data = ss.str();
        ROS_INFO("%s", msg.data.c_str());
        welcome_message_pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}