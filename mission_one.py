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
    # Mission Name PINA Unknown Creature Capture 09
    # Authors= PJOYA THE PINAPANDA
    r.ev3.screen.clear()
    print("Running Mission 1")
    r.ev3.screen.draw_text(30, 60, "Mission 1")
    wait(250)
    r.robot.stop()
    # Mission Name 
    # Authors
    r.gyro_drive_straight_distance(speed=200,distance=500)
    r.gyro_drive_straight_distance(speed=200,distance=-500)
    #r.left_drive_motor.brake()
    #r.right_drive_motor.brake()
    #r.gyro_tank_turn(speed=500, angle=-75)
    #r.gyro_drive_straight_distance(speed=500,distance=270)