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
from robot_18300 import robot_18300

def mission_five(r):
    print("Running Mission 5")
    #madeleine + Lydia going to the museum
    #r.robot.straight(-323)
    r.gyro_drive_straight_distance(-150,373)
    wait(100)
    #r.robot.turn(-45)
    r.gyro_tank_turn(150,-45)
    wait(100)
    #r.robot.straight(-343)
    r.gyro_drive_straight_distance(-150,271)
    wait(100)
    #Robot is facing the set change mission.
    #r.robot.turn(-45)
    r.gyro_tank_turn(150,-40)
    wait(100)
    #r.robot.straight(-391)
    r.gyro_drive_straight_distance(-150,331)
    wait(100)
    #Used to be -321 /\
    #turn torward wall
    #r.robot.turn(90)
    r.robot.drive(-200,76)
    wait(3011)
    #The robot is now at the wall
    r.robot.stop()
    while(r.robot.state()[1]>10):
        wait(10)
    r.robot.straight(160)
    r.robot.turn(23)
    #used to be (291)
    r.robot.drive(60,0)
    wait(1011)
    #The robot is now at the light tower
    r.robot.stop()
    #Backing up
    # \/ Light tower is going up
    r.left_attachment_motor.run_time(-300,10000, then=Stop.HOLD, wait=False)
    wait(5000)
    r.robot.stop()
    #Robot is Facing Augmented reality.
    r.robot.straight(-40)
    #r.robot.turn(35)
    r.gyro_tank_turn(150,30)
    wait(100)
    #r.robot.drive(-75,0)
    #wait(1800)
    #r.robot.stop()
    r.robot.straight(-107)
    #At Augmented reality
    r.gyro_tank_turn(70,37) 
    r.robot.stop()
    r.robot.straight(-123)
    r.robot.turn(-30)
    #Augmented reality is now complreted.
    

    