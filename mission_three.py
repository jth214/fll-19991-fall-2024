################################
# mission_three.py
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

def mission_three(r):
    print("Running Mission 3")
    #jackson yesue rolling camera
    # drive straight into roller coaster
    r.robot.drive(300,-10)
    wait(1500)
    r.robot.stop()
    wait(500)
    r.robot.straight(-350)






  
