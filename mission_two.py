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
    #Wesleys Mission Turn Chicken.
    #drives to skater girl
    r.robot.straight(325)
    r.left_attachment_motor.run_time(300, 90,then=Stop.HOLD, wait=True)
    #drivesto chicken 
    r.robot.straight(90)
    #lifts flap
    r.right_attachment_motor.run_time(300,4000, then=Stop.HOLD, wait=False)     
    #waits 
    wait(3000)
    #backs up and finishes lift flap
    r.robot.straight(-100)
    r.right_attachment_motor.run_angle(-500, 150,then=Stop.HOLD, wait=True)
    r.robot.stop()