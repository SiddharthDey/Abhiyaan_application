//the following code has taken from "http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29" and has been
//modified for the desired output as given in the application
#include "ros/ros.h"
#include "std_msgs/String.h"
void welcome_messageCallback(const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO("[%s]", msg->data.c_str());
}
int main(int argc, char **argv)
{
    //initializing the node
    ros::init(argc, argv, "listener");
    //creating a handle for the current node
    ros::NodeHandle n;
    //the node subsrcibes to tbhe topic "welcome_message"
    ros::Subscriber sub = n.subscribe("welcome_message", 1000, welcome_messageCallback);
    ros::spin();
    return 0;
}