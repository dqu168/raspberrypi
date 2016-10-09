#!/usr/bin/python -tt
import logging
import time
import robot
import ultrasonic_sensor


def main():
    my_car = robot.Robot()
    sensor = ultrasonic_sensor.UltrasonicSensor()
    my_car.cleanup()
    sensor.cleanup()

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s")
    main()
    print "program ends"