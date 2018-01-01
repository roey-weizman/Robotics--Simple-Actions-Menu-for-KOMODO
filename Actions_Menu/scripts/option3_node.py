#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import os
import numpy as np
from std_msgs.msg import String
import sys

red = []


##get minimum distance to red object
def get_min_distance(msg):
  br = CvBridge()
  img = br.imgmsg_to_cv2(msg)
  distances = [img[x][y] for (x, y) in red]
  if sys.argv[1] == '3':
    print('The minimum distance to the red object is {}'.format(min([d for d in distances if not np.isnan(d)])))
  else:
    tmp_file = open("tmp_file.txt", "w")
    tmp_file.write('{}'.format(min([d for d in distances if not np.isnan(d)])))##write desired distance to a file 
  os.system('rosnode kill option3_node')

def find_red(msg):
  global red
  br = CvBridge()
  img = br.imgmsg_to_cv2(msg,'bgr8')
  height, width, depth = img.shape
  img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)# reverse to hsv
  lower_red = np.array([170,120,120])
  upper_red = np.array([180,255,255])#red bound
  mask = cv2.inRange(img_hsv, lower_red, upper_red)#masking to red
  img= cv2.bitwise_and(img, img, mask=mask)#and operation
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  blurred_img = cv2.GaussianBlur(gray, (5, 5), 0)# blurring
  threshold = cv2.threshold(blurred_img, 20, 255, 0)[1]
  for x in range(0, height):##appending desired pixels
    for y in range(0, width):
      if threshold[x][y] == 255:
	red.append((x, y))
  if not red:
    if sys.argv[1] == '3':
      print('No red object')
    else:
      tmp_file = open("tmp_file.txt", "w")
      tmp_file.write('None')
    os.system('rosnode kill option3_node')
  else:
    sub = rospy.Subscriber("/torso_camera/depth_registered/image_raw", Image, get_min_distance)





rospy.init_node('option3_node', anonymous=False)
sub = rospy.Subscriber('/torso_camera/rgb/image_raw', Image, find_red)
rospy.spin()