#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 
import math

def move():
    rospy.init_node('goal_trial_node',anonymous=True)
    pub= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    freq=0.1

    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = 0.3
        vel.angular.z =  math.sin(2 * math.pi * freq * rospy.get_time())  
        pub.publish(vel)

        rate.sleep()


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
