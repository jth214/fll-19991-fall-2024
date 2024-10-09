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
from robot_19991 import robot_19991

def mission_four(r):
    print("Running Mission 4")
    # Mission Name
    # Authors
    r.ev3.screen.clear()
    print("Running Mission 4")
    r.ev3.screen.draw_text(30, 60, "Mission 4")
    wait(time=100)
    # Mission Name: Angler Fish and Unexpected Encounter
    # Authors
    #r.gyro_drive_straight_time(speed=500,time=2000)
    #r.gyro_tank_turn(1050,50)
    #r.gyro_drive_straight_time(speed=500,time=2000)
    r.gyro_drive_straight_distance(speed=500,distance=600)
    r.gyro_drive_straight_distance(speed=500,distance=-600)
