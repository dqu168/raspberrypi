#!/usr/bin/python -tt
import RPi.GPIO as GPIO
import time
import gpio_pins

class Robot:
    def __init__(self):
        self.pin = gpio_pins.GpioPins()
        GPIO.setmode(GPIO.BOARD)
        print "setup GPIO pins for robot"
        GPIO.setup(self.pin.LEFT_MOTOR_FORWARD, GPIO.OUT)
        GPIO.setup(self.pin.LEFT_MOTOR_BACKWARD, GPIO.OUT)
        GPIO.setup(self.pin.RIGHT_MOTOR_FORWARD, GPIO.OUT)
        GPIO.setup(self.pin.RIGHT_MOTOR_BACKWARD, GPIO.OUT)
        self.stop()

    def forward(self):
        GPIO.output(self.pin.LEFT_MOTOR_FORWARD, 1)
        GPIO.output(self.pin.LEFT_MOTOR_BACKWARD, 0)
        GPIO.output(self.pin.RIGHT_MOTOR_FORWARD, 1)
        GPIO.output(self.pin.RIGHT_MOTOR_BACKWARD, 0)
        print "move forward"
        time.sleep(0.1)
    def backward(self):
        GPIO.output(self.pin.LEFT_MOTOR_FORWARD, 0)
        GPIO.output(self.pin.LEFT_MOTOR_BACKWARD, 1)
        GPIO.output(self.pin.RIGHT_MOTOR_FORWARD, 0)
        GPIO.output(self.pin.RIGHT_MOTOR_BACKWARD, 1)
        print "move backward"
        time.sleep(0.1)
    def left(self):
        GPIO.output(self.pin.LEFT_MOTOR_FORWARD, 0)
        GPIO.output(self.pin.LEFT_MOTOR_BACKWARD, 0)
        GPIO.output(self.pin.RIGHT_MOTOR_FORWARD, 1)
        GPIO.output(self.pin.RIGHT_MOTOR_BACKWARD, 0)
        print "turn left"
        time.sleep(0.1)
    def right(self):
        GPIO.output(self.pin.LEFT_MOTOR_FORWARD, 1)
        GPIO.output(self.pin.LEFT_MOTOR_BACKWARD, 0)
        GPIO.output(self.pin.RIGHT_MOTOR_FORWARD, 0)
        GPIO.output(self.pin.RIGHT_MOTOR_BACKWARD, 0)
        print "turn right"
        time.sleep(0.1)
    def stop(self):
        GPIO.output(self.pin.LEFT_MOTOR_FORWARD, 0)
        GPIO.output(self.pin.LEFT_MOTOR_BACKWARD, 0)
        GPIO.output(self.pin.RIGHT_MOTOR_FORWARD, 0)
        GPIO.output(self.pin.RIGHT_MOTOR_BACKWARD, 0)
        print "stop"
        time.sleep(0.1)

    def cleanup(self):
        print "cleanup GPIO pins for robot"
        GPIO.cleanup()


    def test_forward_in_loop(self):
        try:
            while True:
                self.forward()
                time.sleep(1)
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()

    def test_backward_in_loop(self):
        try:
            while True:
                self.backward()
                time.sleep(1)
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()

    def test_left_in_loop(self):
        try:
            while True:
                self.left()
                time.sleep(1)
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()

    def test_right_in_loop(self):
        try:
            while True:
                self.right()
                time.sleep(1)
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()

    def test_forward_right_in_loop(self):
        try:
            while True:
                self.forward()
                time.sleep(2)
                self.right()
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()
