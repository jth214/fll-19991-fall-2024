################################
# mission_five.py
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

def mission_five(r):
    print("Running Mission 5")
    #madeleine going to the museum
    r.robot.straight(564)
    r.robot.turn(-45)
    r.robot.straight(250)
    r.robot.turn(-45)
    r.robot.straight(460)
    r.robot.turn(60)
    r.robot.straight(275)
    r.robot.turn(75)
    r.robot.straight(101)
    speed = 200
    turn = 60
    distance = 136
    r.robot.reset()

    # While the robot.distance() is less than or equal to the variable 'distance' stay in the while loop
    while (r.robot.distance() <= distance):
        r.robot.drive(speed,turn)
    
    
