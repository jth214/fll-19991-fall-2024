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
    r.gyro_drive_straight_distance(speed=500,distance=250)
    r.left_attachment_motor.run_time(speed=500, angle=45, then=Stop.HOLD, wait=True)
    