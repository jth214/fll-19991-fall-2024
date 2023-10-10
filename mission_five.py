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
    r.robot.straight(500)
    r.robot.turn(-45)
    r.robot.straight(250)
    r.robot.turn(-45)
    r.robot.straight(399)
    r.robot.turn(60)
    r.robot.straight(275)
    
    
