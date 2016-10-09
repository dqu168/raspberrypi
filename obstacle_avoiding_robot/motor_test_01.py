#!/usr/bin/python -tt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

LEFT_MOTOR_FORWARD=7
RIGHT_MOTOR_FORWARD=13

GPIO.setup(LEFT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_FORWARD, GPIO.OUT)

for x in range(0,3):
    GPIO.output(LEFT_MOTOR_FORWARD, 1)
    GPIO.output(RIGHT_MOTOR_FORWARD, 1)
    time.sleep(1)
    GPIO.output(LEFT_MOTOR_FORWARD, 0)
    GPIO.output(RIGHT_MOTOR_FORWARD, 0)
    time.sleep(2)

GPIO.cleanup()
