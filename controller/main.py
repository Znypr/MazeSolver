from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase


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


c = Controller()
c.forward()