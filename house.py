def ColorCoding(house1, house2, house3, colorSensor, robot):
    if len(house1) == 0:
        firstColor = colorSensor.color()
        house1 = [firstColor, ColorMoving(robot, colorSensor)]
        return house1
    elif len(house2) == 0:
        firstColor = colorSensor.color()
        house2 = [firstColor, ColorMoving(robot, colorSensor)]
        return house2
    elif len(house3) == 0:
        firstColor = colorSensor.color()
        house3 = [firstColor, ColorMoving(robot.colorSensor)]
        return house3


def ColorMoving(robot, colorSensor):
    robot.reset()
    while robot.distance() > -60:
        robot.drive(-100, 0)
    secondColor = colorSensor.color()
    return secondColor
    
