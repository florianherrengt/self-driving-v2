import RPi.GPIO as GPIO
from time import sleep

left_forward = 17
left_backward = 27
left_speed = 18

right_forward = 22
right_backward = 24
right_speed = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

left_pins = [left_forward, left_backward, left_speed]
right_pins = [right_forward, right_backward, right_speed]
all_pins = left_pins + right_pins

GPIO.setup(all_pins, GPIO.OUT)
GPIO.output(all_pins, GPIO.LOW)

left_pwm = GPIO.PWM(left_speed,100)
right_pwm = GPIO.PWM(right_speed,100)
left_pwm.start(0)
right_pwm.start(0)

def set_movement(enabled, side, direction):
	if side == 'left':
		GPIO.output(left_pins, GPIO.LOW)
	else:
		GPIO.output(right_pins, GPIO.LOW)
	if direction == 'forward':
		pin = left_forward if side == 'left' else right_forward
	else:
		pin = left_backward if side == 'left' else right_backward
	status = GPIO.HIGH if enabled else GPIO.LOW
	GPIO.output(pin, status)

def set_speed(direction, percent):
	pwm = left_pwm if direction == 'left' else right_pwm
	pwm.ChangeDutyCycle(percent)

set_speed('left', 100)
set_speed('rigth', 100)

# set_movement(True, 'left', 'forward')
# sleep(1)
# set_movement(False, 'left', 'forward')
# set_movement(True, 'left', 'backward')
# sleep(1)
# set_movement(False, 'left', 'backward')
# set_movement(True, 'right', 'forward')
# sleep(1)
# set_movement(False, 'right', 'forward')
# set_movement(True, 'right', 'backward')
# sleep(1)
# set_movement(False, 'right', 'backward')

# set_movement(True, 'right', 'forward')
# set_movement(True, 'left', 'forward')
# sleep(2)
# set_movement(True, 'right', 'backward')
# set_movement(True, 'left', 'backward')
# sleep(2)

# set_movement(True, 'left', 'forward')
# sleep(1)
# set_movement(False, 'left', 'forward')
# set_movement(True, 'left', 'backward')
# sleep(1)
# set_movement(False, 'left', 'backward')
# set_movement(True, 'right', 'forward')
# sleep(1)
# set_movement(False, 'right', 'forward')
# set_movement(True, 'right', 'backward')
# sleep(1)
# set_movement(False, 'right', 'backward')

set_movement(True, 'right', 'forward')
set_movement(True, 'left', 'forward')
set_speed('left', 50)
set_speed('right', 50)
sleep(5)
set_speed('left', 100)
set_speed('right', 100)
sleep(5)
set_speed('right', 25)
sleep(5)
set_speed('left', 25)
set_speed('right', 100)
sleep(5)

GPIO.output(all_pins, GPIO.LOW)

GPIO.cleanup()