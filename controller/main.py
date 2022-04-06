from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=135)
unit = 50

def drive():
    robot.straight(unit)

def left():
    robot.turn(90)

def right():
    robot.turn(-90)

def reverse():
    robot.straight(-unit)