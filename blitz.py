from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from house import ColorCoding

counter = 0
firstMeasure = True
secondMeasure = True
rotation = 15
house1 = []
house2 = []
house3 = [] 


def IgnoreLines(ignoreList, robot):
    # 1 - bal
    # 0- jobb
    robot.reset()

    global counter
    print(counter)
    if ignoreList[counter] == 0:

        while robot.distance() < 20:
            robot.drive(150, 0)
        
        robot.reset()
        counter += 1
    
        return "not_right"
    elif ignoreList[counter] == 1:
    
        while robot.distance() < 20:
            robot.drive(150, 0)
        
        robot.reset()
        counter += 1
    
        return "not_left"
    elif ignoreList[counter] == 2:
        robot.reset()
    
        counter += 1
        return "accepted"


def LineFollower(robot, wl_sensor, wr_sensor, middle_sensor, right_motor, colorSensor):
    increase = False
    manualSteering = False
    isSteeringLeft = True
    isSteeringRight = False
    global rotation
    def tereskorigalovacak(wl_sensor,wr_sensor,middle_sensor,robot):
        global isSteeringRight
        global isSteeringLeft

        global rotation
        if wl_sensor.reflection() < 25:
            if IgnoreLines([2, 2, 1, 0, 2], robot) != "not_left":
                wait(10)
                robot.reset()
                while robot.distance() > -10:
                    robot.drive(-100, 0)
                
                robot.turn(-94)
                while robot.distance() < 100:
                    robot.drive(100, 0)
                
                robot.reset()
                isSteeringLeft = True
                isSteeringRight = False
                increase = False
                rotation = 15
            
        elif wr_sensor.reflection() < 25:
            if IgnoreLines([2, 2, 1, 0, 2], robot) != "not_right":
            
                wait(10)
                robot.reset()
                while robot.distance() > -10:
                
                    robot.drive(-100, 0)
                
                robot.turn(90)
                
                while robot.distance() < 100:
                
                    robot.drive(100, 0)
                robot.reset()
                isSteeringLeft = False
                isSteeringRight = True
                increase = False
                rotation = -15
            


    while True:
    
        robot.reset() 

        while isSteeringLeft:
        
            if rotation > 0 and not increase:
            
                while middle_sensor.reflection() <= 18:
                
                    robot.drive(150, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot)
                    FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                    SecondMeasure(robot, middle_sensor, colorSensor)
                rotation = (rotation - 1) * -1
                print(rotation)
                while middle_sensor.reflection() > 18:
                
                    robot.drive(150, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot)
                    FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                    SecondMeasure(robot, middle_sensor, colorSensor)
                rotation = (rotation + 1) * -1
                print(rotation)
            
            else:
            
                increase = True
                while middle_sensor.reflection() <= 18:
                
                    robot.drive(150, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot)
                    FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                    SecondMeasure(robot, middle_sensor, colorSensor)
                rotation = (rotation + 1) * -1
                print(rotation)
                while middle_sensor.reflection() > 18:
                
                    robot.drive(150, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot)
                    FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                    SecondMeasure(robot, middle_sensor, colorSensor)
                rotation = (rotation - 1) * -1
                print(rotation)
            
                if rotation == 15:
                    increase = False
        
        while isSteeringRight:
            print('im here')
        
            if rotation <= 0 and not increase:
            
                while middle_sensor.reflection() <= 18:
                
                    robot.drive(150, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot)
                    FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                    SecondMeasure(robot, middle_sensor, colorSensor)
                rotation = (rotation + 1) * -1
                print(rotation)
                while middle_sensor.reflection() > 18:
                
                    robot.drive(150, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot)
                    FirstMeasure(middle_sensor, colorSensor, wl_sensor, wr_sensor)
                    SecondMeasure(robot, middle_sensor, colorSensor)
                rotation = (rotation - 1) * -1
                print(rotation)
            
                FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                SecondMeasure(robot, middle_sensor, colorSensor)
            else:
            
                increase = True
                while middle_sensor.reflection() <= 18:
                
                    robot.drive(150, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot)
                    FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                    SecondMeasure(robot, house2, middle_sensor, colorSensor)
                rotation = (rotation + 1) * -1
                print(rotation)
                while middle_sensor.reflection() > 18:
                
                    robot.drive(150, rotation)
                    tereskorigalovacak(wl_sensor, wr_sensor, middle_sensor, robot)
                    FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                    SecondMeasure(robot, middle_sensor, colorSensor)
                rotation = (rotation - 1) * -1
                print(rotation)
                FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor)
                SecondMeasure(robot, middle_sensor, colorSensor)
            
                if rotation == 0:
                    increase = False 
                


# 1, 1, 0, 2, 0, 2

def FirstMeasure(middle_sensor, robot, colorSensor, wl_sensor, wr_sensor):
    # print(middle_sensor.color())
    global firstMeasure
    global secondMeasure

    global house1
    global house2
    global house3
    if middle_sensor.color() == Color.RED and firstMeasure:
    
        # print("asd")
        robot.reset()
        while robot.distance() < 130:
            robot.drive(100, 0)
        
        robot.reset()
        while robot.distance() > -205:
            robot.drive(-100, 0)
        
        robot.turn(86)
        robot.reset()
        while robot.distance() < 500:
            robot.drive(150, 0)
        
        robot.reset()
        while robot.distance() > -100:
            robot.drive(-100, 0)
        
        robot.reset()
        house1 = ColorCoding(house1, house2, house3, colorSensor, robot)
        print (house1)
        
        # print(house1)
    
        robot.reset()
        while robot.distance() < 200:
            robot.drive(100, 0)
        if len(house1) != 0:
            if Color.YELLOW in house1:
                FirstToYellow(robot, wl_sensor)
            else:
                FirstToSecond(robot, middle_sensor, wl_sensor, wr_sensor)
        firstMeasure = False
        secondMeasure = True


def FirstToSecond(robot, middle_sensor, wl_sensor, wr_sensor):
    global isSteeringRight
    global isSteeringLeft
    global rotation
    
    robot.reset()
    while not wl_sensor.reflection() < 17:
        robot.drive(-100, 0)
    robot.stop()
    robot.reset()
    robot.turn(90)
    robot.reset()
    while not (wr_sensor.reflection() < 17):
        robot.drive(150, 0)
    robot.reset()
    while robot.distance() > -10:
        robot.drive(-150, 0)
    robot.turn(80)
    robot.reset()
    while robot.distance() < 50:
        robot.drive(150, 0)
    isSteeringRight = True
    isSteeringLeft = False
    increase = False
    rotation = -8


def FirstToYellow(robot, wl_sensor):
    robot.reset()
    while robot.distance() > -60:
        robot.drive(-150, 0)
    robot.turn(90)
    robot.reset()
    while robot.distance() < 350:
        robot.drive(150, 0)
    robot.turn(88)
    robot.reset()
    while robot.distance() < 550:
        robot.drive(150, 0)
    robot.turn(100)
    robot.reset()
    while robot.distance() < 600:
        robot.drive(150, 0)
    robot.stop()    
    robot.reset()
    while robot.distance() < 100:
        robot.drive(150, -15)
    #           :)
    YellowToSecond(wl_sensor, robot)


def YellowToSecond(wl_sensor, robot):
    while not wl_sensor.reflection() < 17:
        robot.drive(-150, 0)
    robot.turn(-90)
    robot.reset()
    while robot.distance() < 60:
        robot.drive(150, 0)
    robot.reset()


def SecondMeasure(robot, middle_sensor, colorSensor):
    global firstMeasure
    global secondMeasure

    global house1
    global house2
    global house3
    if (middle_sensor.color() == Color.RED) and secondMeasure:
        robot.reset()
        while robot.distance() < 130:
            robot.drive(150, 0)
        robot.reset()
        while robot.distance() > -210:
            robot.drive(-150, 0)
        robot.turn(86)
        robot.reset()
        while colorSensor.color() is None:
            robot.drive(150, 0)
        robot.stop()
        robot.reset()
        while robot.distance() < 30:
            robot.drive(150, 0)
        robot.reset()
        house2 = ColorCoding(house1, house2, house3, colorSensor, robot)
        print(house2)
        secondMeasure = False
        firstMeasure = False
        if Color.BLUE in house2:
            SecondToBlue(robot, middle_sensor)
        elif Color.GREEN in house2:
            SecondToGreen(robot, middle_sensor)


def SecondToBlue(robot, middle_sensor):

    global house1
    robot.reset()
    while robot.distance() < 300:
        robot.drive(150, 10)
    robot.turn(165)
    while middle_sensor.color() is not Color.RED:
        robot.drive(150, 10)
    robot.turn(40)
    robot.reset()
    while robot.distance() < 150:
        robot.drive(150, 0)
    if Color.GREEN in house1:
        robot.reset()
        while robot.distance() > -530:
            robot.drive(-150, 0)
        robot.reset()
        robot.turn(-88)
        while robot.distance() < 1161:
            robot.drive(150, -4)
        robot.reset()
        robot.turn(-80)
        while robot.distance() < 620:
            robot.drive(150, 0)
        robot.reset()

def SecondToGreen(robot, middle_sensor):

    global house1
    robot.turn(-90)
    robot.reset()
    while robot.distance() > -650:
        robot.drive(-150, 15)
    robot.reset()
    robot.turn(-60)
    while middle_sensor.color() is not Color.RED:
        robot.drive(150, 3)
    robot.reset()
    while robot.distance() < 130:
        robot.drive(150, 0)
    robot.reset()
    print(house1)
    if Color.BLUE in house1:
        print("David egy buzi")
        robot.reset()
        while robot.distance() > -200:
            robot.drive(-150, 0)
        robot.reset()
        robot.turn(95)
        while robot.distance() < 500:
            robot.drive(150, 0)
        robot.turn(125)
        robot.reset()
        while robot.distance() < 1100:
            robot.drive(150, 5)
        robot.reset()
        while middle_sensor.color() is not Color.RED:
            robot.drive(150, -19)
        robot.reset()
        while robot.distance() < 40:
            robot.drive(150, 0)
        robot.stop()

