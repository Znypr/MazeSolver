from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
import rpyc
import math


DIAMETER = 12.1
WHEEL_RADIUS = 17.8


def establish_connection():

    print('Connecting to server...')
    conn = rpyc.classic.connect('ev3dev')  # host name or IP address of the EV3
    print('Connected.')

    ev3_motor = conn.modules['ev3dev2.motor']
    ev3_sensor = conn.modules['ev3dev2.sensor.lego']
    left = ev3_motor.LargeMotor(ev3_motor.OUTPUT_B)
    right = ev3_motor.LargeMotor(ev3_motor.OUTPUT_C)

    base = ev3_motor.MoveTank(OUTPUT_B, OUTPUT_C)


def get_rotation_distance(degrees):
    return math.pi * DIAMETER * degrees / 360 / WHEEL_RADIUS


def forward():
    base.on_for_rotations(20, 20, 1.8)


def backward():
    base.on_for_rotations(-20, -20, 1.8)


def left_turn():
    base.on_for_rotations(10, -10,  get_rotation_distance(90))


def right_turn():
    base.on_for_rotations(-10, 10,  get_rotation_distance(90))


def move(path):
    for move in path:

        if move == 'f':
            forward()

        elif move == 'b':
            backward()

        elif move == 'l':
            left_turn()

        elif move == 'r':
            right_turn()

        else:
            print('Invalid command')
            break
