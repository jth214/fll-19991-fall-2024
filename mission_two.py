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
from robot_19991 import robot_19991

def mission_two(r):
    print("Running Mission 2")
    # Mission Name
    # Authors
    r.ev3.screen.clear()
    print("Running Mission 2")
    r.ev3.screen.draw_text(30, 60, "Mission 2")
    wait(time=100)
    # Mission Name: Coral nursery and Shark
    r.gyro_drive_straight_distance(speed=200,distance=630)
    r.gyro_tank_turn(speed=50, angle=70)
    r.gyro_drive_straight_distance(speed=200,distance=120)
    r.gyro_drive_straight_distance(speed=200,distance=-75)
    r.gyro_tank_turn(speed=50, angle=-15)
    r.gyro_drive_straight_distance(speed=200,distance=310)
    r.gyro_drive_straight_distance(speed=200,distance=-200)
    r.gyro_tank_turn(speed=50, angle=-60)
    r.gyro_drive_straight_distance(speed=200,distance=-870)