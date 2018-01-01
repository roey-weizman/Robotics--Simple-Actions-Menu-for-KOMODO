import os
import sys
import time

for i in range(0, 13):
  os.system('rosrun assignment2 option3_node.py 4')#invoke red distamnce finder
  tmp_file = open("tmp_file.txt", "r")
  min_distance = tmp_file.read()# read desired distance from file
  if min_distance == 'None':
    os.system('rosrun assignment2 option2_node.py 4')
    time.sleep(1)
  else:
    print('The minimum distance to the red object is {}'.format(float(min_distance)))# print distance to red object
    os.remove('tmp_file.txt')
    sys.exit(0)
os.remove('tmp_file.txt')
  

