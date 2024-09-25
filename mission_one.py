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
from robot_19991 import robot_19991

def mission_one(r):
    print("Running Mission 1")
    # Mission Name
    # Authors
    r.ev3.screen.clear()
    print("Running Mission 1")
    r.ev3.screen.draw_text(30, 60, "Mission 1")
    wait(250)
    r.robot.stop()
    # Mission Name
    # Authors
    # r.gyro_drive_straight_distance(speed=500,distance=1500)
    r.gyro_drive_straight_distance(speed=500,distance=910)
    r.tank_turn(speed=500, angle=20)
    