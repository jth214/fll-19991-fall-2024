################################
# mission_eleven.py
################################

import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_19991 import robot_19991

def mission_eleven(r):  
    print("Running Mission 11")
    # Mission Name
    # Authors
    r.ev3.screen.clear()
    print("Running Mission 11")
    r.ev3.screen.draw_text(30, 60, "Mission 11")
    wait(time=100)
    r.gyro_drive_straight_distance(speed=500,distance=-1050)
    r.gyro_tank_turn(speed=500,angle=85)
    r.gyro_drive_straight_distance(speed=500,distance=100)