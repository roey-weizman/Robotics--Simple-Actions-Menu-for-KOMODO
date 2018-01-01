#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import os
from math import fabs

moved = False
initial_center = None

def move(msg):
  global moved
  global initial_center
  center = msg.ranges[len(msg.ranges)/2] # get the center point from laser
  new_msg = Twist()
  new_msg.linear.x = 0.1
  if not moved:
    rospy.loginfo(center)
    moved = True
    if center >= 0.5:
      initial_center = center
      pub.publish(new_msg)
    else:
      os.system('rosnode kill option1_node')
  else:
    if fabs(fabs(initial_center - center) - 0.5) < 0.1:
      os.system('rosnode kill option1_node')
    pub.publish(new_msg)
    
  
rospy.init_node('option1_node', anonymous=False)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber("/scan", LaserScan, move)
rospy.spin()
