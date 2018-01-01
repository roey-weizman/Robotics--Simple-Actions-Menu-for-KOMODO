#!/usr/bin/env python

import os

while True:
  option = input('please choose an option:\n1. Move forward\n2. Turn around\n3. Distance to red object\n4. Find red object \n')
  if option == 1:#move forward
    os.system('rosrun assignment2 option1_node.py')
  elif option == 2:#turn around
    os.system('rosrun assignment2 option2_node.py 2')
  elif option == 3:#distance to red object
    os.system('rosrun assignment2 option3_node.py 3')
  elif option == 4:#find red object
    os.system('python ' + os.getenv("HOME") + '/catkin_ws/src/assignment2/scripts/option4.py')
  else:
    print('illegal input: {}'.format(option))
	
 
