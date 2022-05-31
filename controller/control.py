#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import GyroSensor
import rpyc

print('Connecting to server...')
conn = rpyc.classic.connect('ev3dev')  # host name or IP address of the EV3
print('Connected.')

ev3_motor = conn.modules['ev3dev2.motor']
ev3_sensor = conn.modules['ev3dev2.sensor.lego']
left = ev3_motor.LargeMotor(ev3_motor.OUTPUT_B)
right = ev3_motor.LargeMotor(ev3_motor.OUTPUT_C)

base = ev3_motor.MoveTank(OUTPUT_B, OUTPUT_C)
#base.gyro = GyroSensor()
# base.gyro.calibrate()


def forward():
    base.on_for_rotations(20, 20, 1.8)


def backward():
    base.on_for_rotations(-20, -20, 1.8)


def left_turn():
    #base.turn_left(30, 90)
    base.on_for_rotations(10, -10,  0.52)


def right_turn():
    #base.turn_right(30, 90)
    base.on_for_rotations(-10, 10,  0.52)


def move(path):

    for step in path:

        if step == 'f':
            forward()
        elif step == 'b':
            backward()
        elif step == 'l':
            left_turn()
        elif step == 'r':
            right_turn()
        else:
            print('Invalid command')
            break
