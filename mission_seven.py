################################
# mission_seven.py
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

def mission_seven(r):  
    print("Running Mission 7")
    #Lydia_and_Madelienes_super_Awesome_code_For_The_Light_Tower
    r.left_attachment_motor.run(800)
    r.right_attachment_motor.run(-800)
    #Both front motors are now spinning to make the light tower go up!
    wait(3000)
    r.left_attachment_motor.stop()
    r.right_attachment_motor.stop()
    