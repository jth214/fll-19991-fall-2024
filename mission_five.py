################################
# mission_five.py
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

def mission_five(r):
    print("Running Mission 5")
    # Mission Name
    # Authors finnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
    r.ev3.screen.clear()
    print("Running Mission 5")
    r.ev3.screen.draw_text(30, 60, "Mission 5")
    wait(time=100)
    # Mission Name - Fins scuba
    # Authors finnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
    #r.left_attachment_motor.run_angle(1500, 90, then=Stop.COAST, wait=True)
    #wait(time=500)
    #r.left_attachment_motor.run_angle(1500, -80, then=Stop.COAST, wait=True)    
    r.gyro_drive_straight_distance(speed=250,distance=640)
    r.gyro_tank_turn(speed=50, angle=90)
    r.left_attachment_motor.run_time(speed=-500, time=5000, then=Stop.HOLD, wait=True)
    
