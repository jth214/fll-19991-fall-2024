################################
# mission_six.py
################################

import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300

def mission_six(r):
    print("Running Mission 6")

     # Create and define distance, speed, and turn variables
    # to control how fast the robot moves, how sharp it turns, and how far it will go.
    # Reset the robot distance to zero
    speed = 200
    turn = 45
    distance = 112
    r.robot.reset()

    # While the robot.distance() is less than or equal to the variable 'distance' stay in the while loop
    while (r.robot.distance() <= distance):
        r.robot.drive(speed,turn)

     # Create and define distance, speed, and turn variables
    # to control how fast the robot moves, how sharp it turns, and how far it will go.
    # Reset the robot distance to zero
    speed = 200
    turn = -60
    distance = 136
    r.robot.reset()

    # While the robot.distance() is less than or equal to the variable 'distance' stay in the while loop
    while (r.robot.distance() <= distance):
        r.robot.drive(speed,turn)
    
    print("The robot has moved " + str(r.robot.distance()) + " mm")

    # r.robot.drive() goes on forever, even after the while loop ends.
    # You need to stop the robot after exiting the while loop
    r.robot.stop()
    
    print("The robot has moved " + str(r.robot.distance()) + " mm")

    # r.robot.drive() goes on forever, even after the while loop ends.
    # You need to stop the robot after exiting the while loop
    r.robot.stop()