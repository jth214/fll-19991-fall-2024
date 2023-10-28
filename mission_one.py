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
    r.robot.stop()
    r.right_attachment_motor.stop()
    r.left_attachment_motor.stop()
    r.right_attachment_motor.reset_angle(0)
    r.left_attachment_motor.reset_angle(0)
    # push down arm
    r.right_attachment_motor.run_angle(300,40, then=Stop.COAST, wait=False)     
    r.left_attachment_motor.run_angle(300, -40, then=Stop.COAST, wait=True)
    # raise arm back up 
    r.right_attachment_motor.run_angle(300,-40, then=Stop.HOLD, wait=False)
    r.left_attachment_motor.run_angle(300, 40, then=Stop.HOLD, wait=True)
    #use gyro to drive straight into 3d theater
    r.gyro_drive_straight_time(150, 2000)
    #use gyro to keep driving straight into 3d theater
    r.gyro_drive_straight_time(100, 1200)
    # Back up        
    r.gyro_drive_straight_time(-100, 1000)
    # move forward agian to push scene change lever
    r.gyro_drive_straight_time(100, 2500)
    #back up so the scene change lever is not being pushed
    r.gyro_drive_straight_time(-100, 500)
    # release lever attachment
    r.right_attachment_motor.run_angle(300,30, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_angle(300, -30, then=Stop.HOLD, wait=False)
    #back awway from lever attachment
    r.gyro_drive_straight_time(-200, 2500)
    r.robot.stop()
    r.robot.reset()
    # line up for the sound mixer mission
    r.robot.straight(35)
    r.robot.turn(45)
    # lower the arm
    r.right_attachment_motor.run_time(100,750, then=Stop.COAST, wait=False)     
    r.left_attachment_motor.run_time(-100,750, then=Stop.COAST, wait=False)
    # drive forward with speed 100 for 4 seconds
    r.robot.drive(100, 0)
    wait(4000)
    r.robot.stop()
    #backup
    r.robot.straight(-10)
    # raise the arm
    r.right_attachment_motor.run_time(-1000,4000, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_time(1000,4000, then=Stop.HOLD, wait=False)
    wait(500)
    # driving forward for 800 miliseconds while lifting arm to raise mixer levers
    r.robot.drive(50,0)
    wait(1200)
    r.robot.stop()
    # turn to the right releasing one at a time and end up facing the south wall
    r.gyro_tank_turn(50,120)
    #lower the arm 
    #r.right_attachment_motor.run_time(200,750, then=Stop.COAST, wait=False)     
    #r.left_attachment_motor.run_time(-200,750, then=Stop.COAST, wait=True)
    # drive straight into sounth wall to sqar up 
    r.robot.drive(180,0)
    wait(1500)
    r.robot.stop()
    # back up 5 cm to make space so the robot can turn.
    r.robot.straight(-50)
    # turn towards roller coster
    r.robot.turn(-50)
    #drive forwards into roller coaster 
    r.robot.drive(100,0)
    wait(1800)
    r.robot.stop()
    # back up 
    r.robot.straight(-10)
    # raise the arm
    r.right_attachment_motor.run_time(-1000,3000, then=Stop.HOLD, wait=False)     
    r.left_attachment_motor.run_time(1000,3000, then=Stop.HOLD, wait=True)
    r.robot.turn(-60)
    r.robot.straight(-120)
    r.robot.straight(20)
    r.right_attachment_motor.run_time(200,1000, then=Stop.COAST, wait=False)     
    r.left_attachment_motor.run_time(-200,1000, then=Stop.COAST, wait=True)
    # back up while pulling the camera loop nto the film strip
    r.robot.drive(-100,-50)
    wait(1000)
    r.robot.stop()
