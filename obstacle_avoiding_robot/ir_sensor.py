#!/usr/bin/python -tt
import RPi.GPIO as GPIO
import gpio_pins
import direction_enum


class IRSensor:

    def __init__(self):
        #instance variables
        self.pin = gpio_pins.GpioPins()
        self.obstacle = direction_enum.DirectionEnum()
        GPIO.setmode(GPIO.BOARD)
        print "setup GPIO pins for ir_sensor"
        GPIO.setup(self.pin.IR_SENSOR_LEFT, GPIO.IN)
        GPIO.setup(self.pin.IR_SENSOR_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    # return direction_enum
    def detectObstacle(self):
        left_ir_value = GPIO.input(self.pin.IR_SENSOR_LEFT)
        right_ir_value = GPIO.input(self.pin.IR_SENSOR_RIGHT)
        # print "left ir value: ", left_ir_value
        # print "right ir value: ", right_ir_value
        if left_ir_value == 0 and right_ir_value == 0:
            di = self.obstacle.FRONT
        elif left_ir_value == 0:
            di = self.obstacle.LEFT
        elif right_ir_value == 0:
            di = self.obstacle.RIGHT
        else:
            di = self.obstacle.NO_OBSTACLE
        return di


    def cleanup(self):
        print "cleanup GPIO pins for sensor"
        GPIO.cleanup()

