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
    # LOWER
    r.right_attachment_motor.run_time(-1000,3000, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_time(1000,3000, then=Stop.HOLD, wait=True)
    wait(2500)
    # RAISE
    r.right_attachment_motor.run_time(1000,3000, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_time(-1000,3000, then=Stop.HOLD, wait=True)
    wait(2500)
    # LOWER
    r.right_attachment_motor.run_time(-1000,3000, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_time(1000,3000, then=Stop.HOLD, wait=True)
    wait(2500)
    # RAISE
    r.right_attachment_motor.run_time(1000,3000, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_time(-1000,3000, then=Stop.HOLD, wait=True)
    wait(2500)