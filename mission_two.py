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
    r.robot.straight(400)
    #drive hard into chicken
    r.robot.drive(200,0)
    wait(1000)
    r.robot.stop()
    #press gently into chicken or else it will get stuck from the force
    r.robot.drive(50,0)
    wait(2000)
    r.robot.stop()
    #lower arm - use coast to make it so the motor does not run while it is down.
    r.right_attachment_motor.run_time(300, 1200,then=Stop.COAST, wait=True)
    #back up and lifts flap
    r.robot.straight(-180)
    # resets the motor angle to zero and raises the arm 
    r.right_attachment_motor.stop()
    r.right_attachment_motor.reset_angle(0)
    r.right_attachment_motor.run_angle(-200, 180,then=Stop.HOLD, wait=True)
    r.robot.turn(45)
    r.robot.straight(350)
    r.robot.drive(100,20)
    wait(2300)
    r.robot.stop()
    # THE ARm lowers to flip the orange lever
    r.right_attachment_motor.run_angle(200, 103,then=Stop.COAST, wait=True)
    wait(1000)
    r.robot.straight(-150)
    r.robot.turn(120)
    r.robot.straight(500)
    #r.robot.drive(-100,-35)
    #wait(1000)
    #r.robot.drive(-400,-55)
    #wait(2000)
    r.right_attachment_motor.run_time(-300, 500,then=Stop.COAST, wait=True)
    r.robot.stop()
    
