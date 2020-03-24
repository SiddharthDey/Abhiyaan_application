//the code is not working but i am not able to figure out why
//I think coding logic is fine but there might be some concepual mistake
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

//the publisher1 class publishes a string to the topic "topic1"  
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

//the class subscriber1 is called when the subscriber in the main function recieves a message from topic1
//and then subscibes to topic1 and saves the obtained string
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

void subscriber_call(){
    subscriber1 subs1;
}

//the main class is the master class which subscribes to topic1 and then calls subscriber1
int main(int argc, char **argv)
{
    ros::init(argc, argv, "controller");
    ros::NodeHandle n;
    publisher1 publ1;
    ros::Subscriber sub2 = n.subscribe("topic1", 1000, subscriber_call);
    return 0;
}

