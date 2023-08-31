#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math

def move_in_circle():
    rospy.init_node('circ_turt_one_node', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Adjust this rate as needed

    twist = Twist()
    twist.linear.x = 1.0  # Linear velocity (m/s)
    twist.angular.z = 1.0  # Angular velocity (rad/s)

    circumference = 2 * math.pi  # Calculate the circumference of the circle
    duration = circumference / twist.linear.x  # Calculate the time needed for one circle

    start_time = rospy.Time.now().to_sec()
    
    while not rospy.is_shutdown():
        current_time = rospy.Time.now().to_sec()
        elapsed_time = current_time - start_time
        
        if elapsed_time < duration:
            pub.publish(twist)
        else:
            # Stop the turtle after one circle
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)
            break
        
        rate.sleep()

if __name__ == '__main__':
    try:
        move_in_circle()
    except rospy.ROSInterruptException:
        pass
