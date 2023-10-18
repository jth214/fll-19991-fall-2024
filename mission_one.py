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
    wait(250)
    r.right_attachment_motor.reset_angle(0)
    r.left_attachment_motor.reset_angle(0)
    r.right_attachment_motor.run_angle(300,40, then=Stop.COAST, wait=False)     
    r.left_attachment_motor.run_angle(300, -40, then=Stop.COAST, wait=True)
    #new
    r.right_attachment_motor.run_angle(300,-40, then=Stop.HOLD, wait=False)
    r.left_attachment_motor.run_angle(300, 40, then=Stop.HOLD, wait=True)
    r.gyro_drive_straight_time(150, 2000)
    #old
    #r.right_attachment_motor.run_angle(300,-40, then=Stop.HOLD, wait=False)
    #r.left_attachment_motor.run_angle(300, 40, then=Stop.HOLD, wait=False)
    r.gyro_drive_straight_time(100, 1200)       
    r.gyro_drive_straight_time(-100, 1000)
    r.gyro_drive_straight_time(100, 2500)
    r.gyro_drive_straight_time(-100, 500)
    r.right_attachment_motor.run_angle(300,30, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_angle(300, -30, then=Stop.HOLD, wait=False)
    r.gyro_drive_straight_time(-200, 2500)
    r.robot.stop()
    r.robot.reset()
    r.robot.straight(35)
    r.robot.turn(45)
    r.right_attachment_motor.run_time(100,750, then=Stop.COAST, wait=False)     
    r.left_attachment_motor.run_time(-100,750, then=Stop.COAST, wait=False)
    r.robot.drive(100, 0)
    wait(4000)
    #r.robot.stop()
    #r.robot.straight(-20)
    r.right_attachment_motor.run_time(-1000,3000, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_time(1000,3000, then=Stop.HOLD, wait=False)
    r.robot.stop()
    wait(200)
    r.robot.drive(50,0)
    wait(800)
    r.robot.stop()
    #turn toward movie camera
    r.gyro_tank_turn(50, 55)
    wait(750)
    r.right_attachment_motor.stop()
    r.left_attachment_motor.stop()
    #robot drives 15.1cm towards camera
    r.robot.straight(140)
    #lower the arm
    r.right_attachment_motor.run_time(100,750, then=Stop.COAST, wait=False)     
    r.left_attachment_motor.run_time(-100,750, then=Stop.COAST, wait=False)
    #drive straight until hit the thigy
    r.robot.drive(100, 0)
    wait(2000)
    r.robot.drive(-50,50)
    wait(3000)