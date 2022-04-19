#!/usr/bin/env python3
from ev3dev2.motor import Motor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.led import Leds
#from ev3dev2.motor import Motor
#from ev3dev2.parameters import Port
#from ev3dev2.robotics import DriveBase

leds = Leds()
leds.set_color("LEFT", "RED")
leds.set_color("RIGHT", "RED")

# TODO: Add code here
'''
class Controller:

    ev3 = EV3Brick()

    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)

    robot = DriveBase(left_motor, right_motor,
                      wheel_diameter=55, axle_track=135)
    unit = 50

    def forward(self):
        self.robot.straight(self.unit)

    def left(self):
        self.robot.turn(90)

    def right(self):
        self.robot.turn(-90)

    def backwards(self):
        self.robot.straight(-self.unit)


def move(actions):

    c = Controller()
    for action in actions:
        if action == 'f':
            c.forward()
        elif action == 'r':
            c.right()
        elif action == 'b':
            c.backwards()
        elif action == 'l':
            c.left()


actions = input("actions:\n")
move(actions)
'''
