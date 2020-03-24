//the following code has taken from "http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29" and has been
//modified for the desired output as given in the application
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
    //initializing the node
    ros::init(argc, argv, "talker");
    //creating a handle for the current node
    ros::NodeHandle n;
    //the node publishes a string to the topic "welcome_message"
    ros::Publisher welcome_message_pub = n.advertise<std_msgs::String>("welcome_message", 1000);
    ros::Rate loop_rate(10);
    while (ros::ok())
    {
        std_msgs::String msg;
        std::stringstream ss;
        //the message published is "Welcome to Abhiyaan"
        ss << "Welcome to Abhiyaan";
        msg.data = ss.str();
        ROS_INFO("%s", msg.data.c_str());
        welcome_message_pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}