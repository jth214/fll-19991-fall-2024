################################
# mission_ten.py
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

def mission_ten(r):  
    print("Running Mission 10")
    # Mission Name - Kraken's Treasure
    # Authors - Fin
    r.ev3.screen.clear()
    print("Running Mission 10")
    r.ev3.screen.draw_text(30, 60, "Mission 10")
    wait(time=100)