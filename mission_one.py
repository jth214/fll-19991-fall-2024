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
    r.right_attachment_motor.reset_angle(0)
    r.left_attachment_motor.reset_angle(0)
    r.right_attachment_motor.run_angle(300,30, then=Stop.HOLD, wait=False)
    r.left_attachment_motor.run_angle(300, -30, then=Stop.HOLD, wait=False)
    wait(3000)
    r.right_attachment_motor.run_angle(300,-30, then=Stop.HOLD, wait=False)
    r.left_attachment_motor.run_angle(300, 30, then=Stop.HOLD, wait=False)
    r.gyro_drive_straight_time(10, 5500)       
    r.gyro_drive_straight_time(10, 2500)       
    r.robot.stop()
 