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
    #madeleine + Lydia going to the museum
    r.robot.straight(-323)
    r.robot.turn(-45)
    r.robot.straight(-343)
    #Robot is facing the set change mission.
    r.robot.turn(-45)
    r.robot.straight(-501)
    #turn torward wall
    r.robot.turn(90)
    r.robot.drive(-200,0)
    wait(1111)
    #The robot is now at the wall
    r.robot.stop()
    r.robot.straight(112)
    #Backing up
    r.robot.turn(37)
    r.robot.stop()
    #Robot is Facing Augmented reality.
    r.robot.drive(-75,0)
    wait(2000)
    r.robot.stop()
    #At Augmented reality
    r.gyro_tank_turn(70,50) 
    r.robot.stop()
    r.robot.straight(-123)
    r.robot.turn(-30)
    #Augmented reality is now complreted.
    