#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

class publisher1{
    public:
    publisher1(){
        ros::NodeHandle n;
        ros::Publisher pub1 = n.advertise<std_msgs::String>("topic1", 1000);
        std_msgs::String msg;
        std::stringstream ss;
        ss << "Welcome to Abhiyaan";
        msg.data = ss.str();
        pub1.publish(msg);
        ros::spinOnce();
    }
};

class subscriber1{
    public:
    void welcome_messageCallback(const std_msgs::String::ConstPtr& msg){
        ROS_INFO("[%s]", msg->data.c_str());
    }

    subscriber1(){
        ros::NodeHandle n;
        ros::Subscriber sub1 = n.subscribe("topic1", 1000, welcome_messageCallback);
        ros::spinOnce();
    }
};
//the main class is the master class
int main(int argc, char **argv)
{
    ros::init(argc, argv, "controller");
    ros::NodeHandle n;
    publisher1 publ1;
    ros::Subscriber sub2 = n.subscribe("topic1", 1000, subscriber1 subs1);
    return 0;
}

