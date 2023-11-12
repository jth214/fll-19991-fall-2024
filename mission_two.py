################################
# mission_two.py
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

def mission_two(r):
    print("Running Mission 2")
    #Wesleys Mission Turn Chicken.
    #drives to skater girl
    r.robot.straight(415)
    r.right_attachment_motor.run_time(300, 1000,then=Stop.HOLD, wait=True)
    #lifts flap
    r.robot.straight(-650)