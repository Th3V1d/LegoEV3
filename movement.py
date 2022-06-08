#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from house import ColorCoding
counter = 0




def Hold(motor):
    if motor.angle() > 5:
        motor.run_target(200, -1)


def IgnoreLines(ignoreList, robot, middle_motor):
    # 1 - bal
    # 0- jobb
    robot.reset()
    Hold(middle_motor)
    global counter
    print(counter)
    if ignoreList[counter] == 0:
        Hold(middle_motor)
        while robot.distance() < 20:
            robot.drive(100, 0)
            Hold(middle_motor)
        robot.reset()
        counter += 1
        Hold(middle_motor)
        return "not_right"
    elif ignoreList[counter] == 1:
        Hold(middle_motor)
        while robot.distance() < 20:
            robot.drive(100, 0)
            Hold(middle_motor)
        robot.reset()
        counter += 1
        Hold(middle_motor)
        return "not_left"
    elif ignoreList[counter] == 2:
        robot.reset()
        Hold(middle_motor)
        counter += 1
        return "accepted"


def LineFollower(robot, middle_motor, wl_sensor, wr_sensor, middle_sensor, right_motor, house1, house2, house3, colorSensor, catcher_motor):
    original_rotation = 15
    rotation = original_rotation
    increase = False
    isSteeringLeft = True
    isSteeringRight = False
    while True:
        Hold(middle_motor)
        robot.reset() 

        while isSteeringLeft:
            Hold(middle_motor)
            if rotation > 0 and not increase:
                Hold(middle_motor)
                while middle_sensor.reflection() <= 18:
                    Hold(middle_motor)
                    robot.drive(100, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot, middle_motor)
                    HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor  )
                rotation = (rotation - 1) * -1
                print(rotation)
                while middle_sensor.reflection() > 18:
                    Hold(middle_motor)
                    robot.drive(100, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot, middle_motor)
                    HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                rotation = (rotation + 1) * -1
                print(rotation)
                HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                Hold(middle_motor)
            else:
                Hold(middle_motor)
                increase = True
                while middle_sensor.reflection() <= 18:
                    Hold(middle_motor)
                    robot.drive(100, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot, middle_motor)
                    HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                rotation = (rotation + 1) * -1
                print(rotation)
                while middle_sensor.reflection() > 18:
                    Hold(middle_motor)
                    robot.drive(100, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot, middle_motor)
                    HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                rotation = (rotation - 1) * -1
                print(rotation)
                HouseAndMeasurments(middle_sensor, robot, house1, house2, house3,colorSensor, middle_motor, catcher_motor)
                Hold(middle_motor)
                if rotation == 15:
                    increase = False
        
        while isSteeringRight:
            print('im here')
            Hold(middle_motor)
            if rotation <= 0 and not increase:
                Hold(middle_motor)
                while middle_sensor.reflection() <= 18:
                    Hold(middle_motor)
                    robot.drive(100, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot, middle_motor)
                    HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                rotation = (rotation + 1) * -1
                print(rotation)
                while middle_sensor.reflection() > 18:
                    Hold(middle_motor)
                    robot.drive(100, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot, middle_motor)
                    HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                rotation = (rotation - 1) * -1
                print(rotation)
                Hold(middle_motor)
                HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
            else:
                Hold(middle_motor)
                increase = True
                while middle_sensor.reflection() <= 18:
                    Hold(middle_motor)
                    robot.drive(100, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot, middle_motor)
                    HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                rotation = (rotation + 1) * -1
                print(rotation)
                while middle_sensor.reflection() > 18:
                    Hold(middle_motor)
                    robot.drive(100, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot, middle_motor)
                    HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                rotation = (rotation - 1) * -1
                print(rotation)
                HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor)
                Hold(middle_motor)
                if rotation == 0:
                    increase = False 


# 1, 1, 0, 2, 0, 2

def tereskorigalovacak(wl_sensor,wr_sensor,middle_sensor,robot, middle_motor):
    global isSteeringRight
    global isSteeringLeft
    if wl_sensor.reflection() < 20:
        if IgnoreLines([2, 2, 1], robot, middle_motor) != "not_left":
            Hold(middle_motor)
            wait(10)
            robot.reset()
            while robot.distance() > -10:
                robot.drive(-100, 0)
                Hold(middle_motor)
            robot.turn(-90)
            while robot.distance() < 100:
                robot.drive(100, 0)
                Hold(middle_motor)
            rotation = 15
            robot.reset()
            isSteeringLeft = True
            isSteeringRight = False
            increase = False
            rotation = 15
            Hold(middle_motor)
    elif wr_sensor.reflection() < 20:
        if IgnoreLines([2, 2, 1], robot, middle_motor) != "not_right":
            Hold(middle_motor)
            wait(10)
            robot.reset()
            while robot.distance() > -10:
                Hold(middle_motor)
                robot.drive(-100, 0)
            robot.turn(88)
            while robot.distance() < 100:
                Hold(middle_motor)
                robot.drive(100, 0)
            rotation = 15
            robot.reset()
            isSteeringLeft = False
            isSteeringRight = True
            increase = False
            rotation = -15
            Hold(middle_motor)


def HouseAndMeasurments(middle_sensor, robot, house1, house2, house3, colorSensor, middle_motor, catcher_motor):
    # print(middle_sensor.color())
    ev3 = EV3Brick()
    if middle_sensor.color() == Color.RED:
        Hold(middle_motor)
        # print("asd")
        robot.reset()
        while robot.distance() < 130:
            robot.drive(100, 0)
            Hold(middle_motor)
        robot.reset()
        while robot.distance() > -200:
            robot.drive(-100, 0)
            Hold(middle_motor)
        robot.turn(89)
        robot.reset()
        while robot.distance() < 500:
            robot.drive(150, 0)
            Hold(middle_motor)
        robot.reset()
        while robot.distance() > -100:
            robot.drive(-100, 0)
            Hold(middle_motor)
        robot.reset()
        if len(house2) == 0:
            house1 = ColorCoding(house1, house2, house3, colorSensor, robot, middle_motor)
            Hold(middle_motor)
        elif len(house3) == 0:
            house2 = ColorCoding(house1, house2, house3, colorSensor, robot, middle_motor)
            Hold(middle_motor)
        else:
            house3 = ColorCoding(house1, house2, house3, colorSensor, robot, middle_motor)
            Hold(middle_motor)
        print(house1)
        Hold(middle_motor)
        robot.reset()
        while robot.distance() < 200:
            robot.drive(100, 0)
        if len(house1) != 0:
            if Color.GREEN in house1 or Color.GREEN in house1:
                GreenWhen2(robot, middle_motor, catcher_motor, middle_sensor)
            if Color.YELLOW in house1:
                YellowWhen2(robot)
            BackToStart(robot, middle_motor)


def GreenWhen2(robot, middle_motor, catcher_motor, middle_sensor):
    robot.reset()
    while robot.distance() > -740:
        robot.drive(-100, -1.99)
    robot.stop()
    middle_motor.reset_angle(0)
    middle_motor.run_target(60, 26.3)
    catcher_motor.run_target(100, 200)
    middle_motor.run_target(100, 0)
    Hold(middle_motor)
    robot.reset()
    while not (middle_sensor.reflection() <= 16):
        robot.drive(100, 1.99)
        Hold(middle_motor)
    robot.stop()
    middle_motor.run_target(60, 70)
    catcher_motor.run_target(100, 0)
    middle_motor.run_target(60, 0)
    while robot.distance() > 0:
        robot.drive(-100, 0.75)
        Hold(middle_motor)
    while robot.distance() > -95:
        robot.drive(-100, 0.7+
        )
    robot.stop()
    robot.reset()
    robot.stop()
    middle_motor.run_target(60, 26.3)
    catcher_motor.run_target(100, 200)
    middle_motor.run_target(100, 0)
    robot.stop()
    robot.reset()
    while not (middle_sensor.reflection() <= 16):
        robot.drive(100, -2)
        Hold(middle_motor)
    robot.reset()
    while robot.distance() < 20:
        robot.drive(100, 0)
    robot.stop()
    middle_motor.run_target(60, 70)
    catcher_motor.run_target(100, 0)
    middle_motor.run_target(60, 0)
    robot.reset()
    robot.turn(-70)
    while robot.distance() < 200:
        robot.drive(100, 0)
    robot.reset()
    while robot.distance() > -150:
        robot.drive(-100, 0)
      


def YellowWhen2(robot):
    robot.reset()
    robot.turn(180)
    while robot.distance() < 480:
        robot.drive(100, 0)
    robot.reset()
    robot.turn(87)
    while robot.distance() < 200:
        robot.drive(150, 0)
    while robot.distance() > 50:
        robot.drive(-100, 0)
    robot.reset()
    robot.turn(-100)
    robot.reset()
    while robot.distance() < 280:
        robot.drive(100, 1)
    robot.reset()
    robot.turn(-195)
    while robot.distance() < 1000:
        robot.drive(200, 0)

def BackToStart(robot, middle_motor):
    robot.reset()
    while robot.distance() > -300:
        robot.drive(-150, 0)
    robot.turn(90)
    robot.reset()
    while robot.distance() < 500:
        robot.drive(150, 0)
    robot.reset()
    while robot.distance() > -70:
        robot.drive(-150, 0)
    robot.turn(85.5)
    robot.reset()
    while robot.distance() < 700:
        robot.drive(150, 0)
    robot.reset()
    while robot.distance() > -40:
        robot.drive(-150, 0)
    robot.reset()
    robot.turn(-90)
    while robot.distance() < 100:
        robot.drive(150, 0)
    robot.reset()
    while robot.distance() > -40:
        robot.drive(-100, 0)
    robot.stop()
    middle_motor.reset_angle(0)
    middle_motor.run_target(100, -70)
    wait(100000000000)

    

