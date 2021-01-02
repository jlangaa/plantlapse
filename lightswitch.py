## Cycles the light switch using a servo
import sys
import time
import RPi.GPIO as GPIO

servo_pin = 17

state = 'on'

try:
    state = sys.argv[1]
except IndexError:
    print('please specify a state')
    exit

pinstate = {'off': 5, 'on': 10}
duty_cycle = pinstate[state]

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm_servo = GPIO.PWM(servo_pin, 50) ## 50hz
pwm_servo.start(duty_cycle)
time.sleep(1)

GPIO.cleanup()
