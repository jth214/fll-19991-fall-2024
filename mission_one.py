################################
# mission_one.py
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

def mission_one(r):
    print("Running Mission 1")
    # 3d theater - john and kyle
    #r.robot.settings(straight_speed=300, straight_acceleration=500, turn_rate=200, turn_acceleration=123)
    r.robot.straight(300)
    r.robot.straight(-400)
    #r.robot.settings(straight_speed=600, straight_acceleration=500, turn_rate=200, turn_acceleration=123)