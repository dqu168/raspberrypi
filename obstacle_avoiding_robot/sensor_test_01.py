#!/usr/bin/python -tt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG=18
ECHO=16

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG, 0)
time.sleep(0.1)
print "start measurement.."
GPIO.output(TRIG, 1)
time.sleep(0.00001)
GPIO.output(TRIG, 0)

while GPIO.input(ECHO) == 0:
    pass
start = time.time()
while GPIO.input(ECHO) == 1:
    pass
stop = time.time()

print (stop-start)*17000  #distance in cm
GPIO.cleanup()
