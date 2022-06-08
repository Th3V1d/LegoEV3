#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import blitz

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

        
# Create your objects here.
left_motor = Motor(Port.A)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, axle_track=170, wheel_diameter=55)
# middle_motor = Motor(Port.B)
# catcher_motor = Motor(Port.D)
middle_sensor = ColorSensor(Port.S3)
wl_sensor = ColorSensor(Port.S2)
wr_sensor = ColorSensor(Port.S1)
colorSensor = ColorSensor(Port.S4)
middle_sensor = ColorSensor(Port.S3)
counter = 0


# # Write your program here. 
while robot.distance() < 200:
    robot.drive(100, 0)
robot.reset() 
blitz.LineFollower(robot, wl_sensor, wr_sensor, middle_sensor, right_motor, colorSensor)
# blitz.SecondMeasure(robot, house2, middle_sensor, colorSensor, house1, house3)
# movement.GreenWhen2(robot, middle_motor, catcher_motor, middle_sensor)

# HouseAndMeasurments()