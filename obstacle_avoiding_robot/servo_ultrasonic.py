import RPi.GPIO as GPIO
import gpio_pins
import direction_enum
import ultrasonic_sensor
import time


class ServoUltraSonic:

    def __init__(self):
        #instance variables
        self.pin = gpio_pins.GpioPins()
        GPIO.setmode(GPIO.BOARD)
        print "setup GPIO pins for ultrasoinic sensor servo"
        GPIO.setup(self.pin.SERVO_ULTRASONIC_SENSOR, GPIO.OUT)

    def cleanup(self):
        print "cleanup GPIO pins for ultrasoinic sensor servo"
        GPIO.cleanup()

    def go_around(self):
        pwm = GPIO.PWM(self.pin.SERVO_ULTRASONIC_SENSOR, 50)  # pwm is Pulse Width Modulation
        pwm.start(7)

        for i in range(0, 180):
            DC = (1.0/18.0)*i+2
            pwm.ChangeDutyCycle(DC)
            time.sleep(0.0015)
            if i == 0 or i == 90 or i == 180:
                print("In go_around 0-180, i = %s" % (i))
                time.sleep(0.5)
        for i in range(180, 0, -1):
            DC = (1.0/18.0)*i+2
            pwm.ChangeDutyCycle(DC)
            if i == 0 or i == 90 or i == 180:
                print("In go_around 180-0, i = %s" % (i))
                time.sleep(0.5)

        pwm.stop()

    def test_go_around(self):
        try:
            self.go_around()
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()

    # ultrasonic sensor making 3 measurements
    def findpath(self, sensor):
        pwm = GPIO.PWM(self.pin.SERVO_ULTRASONIC_SENSOR, 50)  # pwm is Pulse Width Modulation
        pwm.start(7)

        dict = {}
        for i in range(0, 180):
            DC = (1.0 / 18.0) * i + 2
            pwm.ChangeDutyCycle(DC)
            time.sleep(0.0015)
            if i == 0 or i == 90 or i == 180:
                r = sensor.measure_average()
                print("In findpath 0-180, i = %s and measurement result = %s " % (i, r))
                dict[i] = r
                time.sleep(0.5)
        for i in range(180, 0, -1):
            DC = (1.0 / 18.0) * i + 2
            pwm.ChangeDutyCycle(DC)
            if i == 0 or i == 90 or i == 180:
                r = sensor.measure_average()
                print("In findpath 180-0, i = %s and measurement result = %s " % (i, r))
                dict[i] = r
                time.sleep(0.5)

        pwm.stop()

        dir_num = max(dict, key=lambda key: dict[key])
        ret = direction_enum.DirectionEnum().NOWHERE
        if dir_num == 0:
            ret = direction_enum.DirectionEnum().RIGHT
        elif dir_num == 90:
            ret = direction_enum.DirectionEnum().FRONT
        elif dir_num == 180:
            ret = direction_enum.DirectionEnum().LEFT

        return ret


    def test_findpath(self):
        try:
            sensor = ultrasonic_sensor.UltrasonicSensor()
            ret = self.findpath(sensor)
            print("sensor returned value is %s" % (ret))
        except KeyboardInterrupt as e:
            print e
        finally:
            self.cleanup()
