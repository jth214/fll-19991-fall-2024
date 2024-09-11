''' 
Large Motors (wheels):
    Minimum speed = 50
    Maximum speed = 1050

Medium Motors (attachments):
    Minimum speed = 50
    Maximum speed = 1560

All Motors:
    stop() = glide to a stop
    brake() = friction stop then release
    hold() = stop and keep holding stopped

Times are always in milliseconds
Angles are always in degrees

Stop.COAST = let the motor move freely
Stop.BRAKE = passive braking
Stop.HOLD = keep the motor at the stopped angle
'''
r.robot.stop() 
r.robot.brake()
r.robot.hold()

wait(time)

r.robot.calibrate_gyro(port_number which is 4):
r.robot.gyro_tank_turn(speed, angle):
        ''' Tank turn using the gyro
            angle positive = clockwise
            angle negative = counter-clockwise
            speed minimum 50 maximum 1050 
        '''
r.robot.gyro_drive_straight_distance(speed, distance):
        ''' Drive straight using the gyro.
            speed min 50 max 1050
            distance in mm
        '''
r.robot.gyro_drive_straight_time(speed, time):
        ''' Drive straight using the gyro.
            speed min 50 max 1050
            time in ms
        '''
r.left_attachment_motor.run_(speed)
r.right_attachment_motor.run_(speed)

r.left_attachment_motor.run_time(speed, time, then=Stop.HOLD, wait=True)
r.right_attachment_motor.run_time(speed, time, then=Stop.HOLD, wait=True)

r.left_attachment_motor.run_angle(speed, angle, then=Stop.HOLD, wait=True)
r.right_attachment_motor.run_angle(speed, angle, then=Stop.HOLD, wait=True)

r.left_attachment_motor.run_target(speed, angle, then=Stop.HOLD, wait=True)
r.right_attachment_motor.run_target(speed, angle, then=Stop.HOLD, wait=True)
''' Note the difference between run_angle and run_target one is relative and one is absolute
    so if the motor gets messed up run angle will rotate whatever you say but run_target
    will stop when it gets to the angle you want'''
