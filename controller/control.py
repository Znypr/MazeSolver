from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
import rpyc

print('Connecting to server...')
conn = rpyc.classic.connect('ev3dev')  # host name or IP address of the EV3
print('Connected.')

ev3 = conn.modules
print(ev3)
right = ev3.LargeMotor('outB')
left = ev3.LargeMotor('outC')
#base = ev3.DriveBase(left, right, wheel_diameter=56.0, axle_track=114.0)

t = MoveTank(left, right)

def forward():
    t.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 1)
    # base.straight(100)


def backward():
    base.straight(-100)


def left_turn():
    base.turn(90)


def right_turn():
    base.turn(-90)


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
