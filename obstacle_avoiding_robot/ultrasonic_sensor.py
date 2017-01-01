#!/usr/bin/python -tt
import RPi.GPIO as GPIO
import gpio_pins
import time

class UltrasonicSensor:


    def __init__(self):
        #instance variables
        pin = gpio_pins.GpioPins()
        self.trigger = pin.ULTRASONIC_SENSOR_TRIG
        self.echo = pin.ULTRASONIC_SENSOR_ECHO
        self.servo_pin = pin.SERVO_ULTRASONIC_SENSOR
        self.MAX_ELAPSE_TIME = 3  # 3 seconds
        GPIO.setmode(GPIO.BOARD)
        print "setup GPIO pins for ultrasonic_sensor"
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)


    def measure(self):
        # This function measures a distance in cm
        # Return 0 if seeing no obstacle
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)     #send trigger sound pulse for 10ms
        GPIO.output(self.trigger, False)

        timer = time.time()
        while GPIO.input(self.echo) == 0:
            if(time.time() - timer > self.MAX_ELAPSE_TIME):
                return 0
            else:
                pass

        start = time.time()     #first time the sensor hears the sound
        while GPIO.input(self.echo) == 1:
            pass
        stop = time.time()      #last time the sensor hears the sound

        #time for echo is proportional to the distance
        distance = (stop - start) * (34300/2)
        return distance

    def measure_average(self):
        # This function returns the average of 3 measurements
        dist1 = self.measure()
        time.sleep(0.1)
        dist2 = self.measure()
        time.sleep(0.1)
        dist3 = self.measure()
        distance = (dist1 + dist2 + dist3) / 3
        return distance


    def cleanup(self):
        print "cleanup GPIO pins for ultrasonic_sensor"
        GPIO.cleanup()


    def test_measure_in_loop(self):
        try:
            while True:
                distance = self.measure()
                print "Distance : %.1f cm" % distance
                time.sleep(1)
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()


    def test_measure_average_in_loop(self):
        try:
            while True:
                distance = self.measure_average()
                print "Average distance : %.1f cm" % distance
                time.sleep(1)
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()
