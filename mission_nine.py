################################
# mission_nine.py
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

def mission_nine(r):  
    print("Running Mission 9")
    # Mission Name Drive Across
    # Authors
    r.ev3.screen.clear()
    print("Running Mission 9")
    r.ev3.screen.draw_text(30, 60, "Mission 9")
    wait(time=100)
    r.gyro_drive_straight_distance(speed=700,distance=1800)