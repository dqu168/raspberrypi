#!/usr/bin/python -tt
import logging
import time
import robot
import ultrasonic_sensor


def main():
    sensor = ultrasonic_sensor.UltrasonicSensor()
    my_robot = robot.Robot()

    try:
        while True:
            distance = sensor.measure_average()
            print "Obstacle distance : %.1f" % distance
            if distance > 20.0:
                print "no obstacle"
                my_robot.forward()
            else:
                print "see an obstacle"
                my_robot.stop()
                my_robot.backward()
                time.sleep(2)
                my_robot.right()
                time.sleep(2)
            time.sleep(1)
    except KeyboardInterrupt as e:
        print e
    finally:
        sensor.cleanup()
        my_robot.cleanup()


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s")
    main()
    print "program ends"