# Robotics--Simple-Actions-Menu-for-KOMODO
Robotics with Ros Operating System and Catkin_Ws workspace

In this program we build a simple textual user interface that asks for a command number and performs the appropriate command. 
There are four commands you need to implement in this order:
Move forward
Turn around
Distance to red object
Find red object

(1) Move forward moves the robot forward 50cm if there is no obstacle that is closer than 50 cm. Otherwise, the robot does not move.
(2) Prompts for an angle alpha and turns around the robot in place alpha degrees clockwise.
(3) Distance to red object return the distance to a red object in the robot's current frame. If there are no red objects is return NULL. You can assume there is a single red object in the frame, at most.
(4) Find red object turns around while searching for a red object. It stops after it finds a red object and returns its distance. If there is no red object, it stops after doing a full circle.

In order to use it install ROS OS & Castkin_Ws at:
http://wiki.ros.org/ROS/Installation
