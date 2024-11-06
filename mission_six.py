################################
# mission_six.py
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

def mission_six(r):
    print("Running Mission 6")
    # Mission Name  PINA Change Shipping Lanes
    # Authors PJOYA PINAPANDA
    r.ev3.screen.clear()
    print("Running Mission 6")
    r.ev3.screen.draw_text(30, 60, "Mission 6")
    wait(time=100)
    # Mission Name
    # Authors
    r.gyro_drive_straight_distance(speed=500,distance=350)
    #r.left_attachment_motor.run_angle(speed=500, rotation_angle=-45, then=Stop.HOLD, wait=True)
    #r.left_attachment_motor.stop()
    r.gyro_tank_turn(speed=500,angle=-10)
   # r.gyro_drive_straight_distance(speed=500,distance=30)
   # r.left_attachment_motor.run_angle(speed=500, rotation_angle=150, then=Stop.HOLD, wait=True)
   # r.left_attachment_motor.stop()
   # r.gyro_drive_straight_distance(speed=500,distance=-500)
   # r.gyro_tank_turn(speed=500,angle=45)
   # r.gyro_drive_straight_distance(speed=500,distance=200)