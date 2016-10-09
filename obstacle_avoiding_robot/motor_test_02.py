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

print "left motor forward"
GPIO.output(LEFT_MOTOR_FORWARD,1)
time.sleep(2)
GPIO.output(LEFT_MOTOR_FORWARD,0)

print "left motor backward"
GPIO.output(LEFT_MOTOR_BACKWARD,True)
time.sleep(2)
GPIO.output(LEFT_MOTOR_BACKWARD,False)

print "right motor forward"
GPIO.output(RIGHT_MOTOR_FORWARD,True)
time.sleep(2)
GPIO.output(RIGHT_MOTOR_FORWARD,False)

print "right motor backward"
GPIO.output(RIGHT_MOTOR_BACKWARD,True)
time.sleep(2)
GPIO.output(RIGHT_MOTOR_BACKWARD,False)

GPIO.cleanup()
