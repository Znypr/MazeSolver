import rpyc

# Create a RPyC connection to the remote ev3dev device.
# Use the hostname or IP address of the ev3dev device.
# If this fails, verify your IP connectivty via ``ping X.X.X.X``
conn = rpyc.classic.connect('X.X.X.X')

# import ev3dev2 on the remote ev3dev device
motor = conn.modules['ev3dev2.motor']
sensor = conn.modules['ev3dev2.sensor']
sensor_lego = conn.modules['ev3dev2.sensor.lego']

# Use the LargeMotor
left = motor.LargeMotor(motor.OUTPUT_B)
right = motor.LargeMotor(motor.OUTPUT_C)

base = motor.MoveTank(left, right)

base.on_for_seconds(20, 20, 1)