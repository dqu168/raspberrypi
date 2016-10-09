#!/usr/bin/python -tt
import logging
import time
import robot
import ultrasonic_sensor


def main():
    sensor = ultrasonic_sensor.UltrasonicSensor()
    sensor.test_measure_average_in_loop()

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s")
    main()
    print "program ends"