import rpyc
print('Connecting to server...')
conn = rpyc.classic.connect('ev3dev')  # host name or IP address of the EV3
print('Connected.')

ev3 = conn.modules['ev3dev.ev3']

right = ev3.LargeMotor('outB')
left = ev3.LargeMotor('outC')


def forward():
    right.run_forever(speed_sp=500)
    left.run_forever(speed_sp=500)


def backward():
    right.run_forever(speed_sp=-500)
    left.run_forever(speed_sp=-500)


def stop():
    right.stop()
    left.stop()


def left_turn():
    right.run_forever(speed_sp=500)
    left.run_forever(speed_sp=-500)


def right_turn():
    right.run_forever(speed_sp=-500)
    left.run_forever(speed_sp=500)


def move():
    forward()
    stop()


def test():
    print('Testing...')
