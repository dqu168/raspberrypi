#!/usr/bin/python -tt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

LEFT_MOTOR_FORWARD=7
LEFT_MOTOR_BACKWARD=11
RIGHT_MOTOR_FORWARD=13
RIGHT_MOTOR_BACKWARD=15

GPIO.setup(LEFT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_BACKWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_BACKWARD, GPIO.OUT)


try:
    while True:
        print "Rotating both motors in clockwise direction"
        GPIO.output(LEFT_MOTOR_FORWARD,True)
        GPIO.output(LEFT_MOTOR_BACKWARD, False)
        GPIO.output(RIGHT_MOTOR_FORWARD, True)
        GPIO.output(RIGHT_MOTOR_BACKWARD, False)
        time.sleep(5)
        print "Rotating both motors in counterclockwise direction"
        GPIO.output(LEFT_MOTOR_FORWARD,False)
        GPIO.output(LEFT_MOTOR_BACKWARD, True)
        GPIO.output(RIGHT_MOTOR_FORWARD, False)
        GPIO.output(RIGHT_MOTOR_BACKWARD, True)
        time.sleep(5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
