################################
# mission_four.py
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

def mission_four(r):
    print("Running Mission 4")
    # raise the arm
    #r.right_attachment_motor.run_time(-1000,4000, then=Stop.HOLD, wait=False)     
    #r.left_attachment_motor.run_time(1000,4000, then=Stop.HOLD, wait=False)
    #wait(5000)
    # lowe the arm
    #r.right_attachment_motor.run_time(200,4000, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_time(-300,6000, then=Stop.HOLD, wait=False)
    wait(5000)