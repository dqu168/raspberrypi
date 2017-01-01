#!/usr/bin/python -tt
import logging
import time
import robot
import ir_sensor
import direction_enum
import ultrasonic_sensor
import servo_ultrasonic

def main():
    ir = ir_sensor.IRSensor()
    mycar = robot.Robot()
    ultrasonic = ultrasonic_sensor.UltrasonicSensor()
    try:
        while True:
            r = ultrasonic.measure_average()
            print "ultrasonic sensor detects obstacle at %.1f cm " % r
            if r < 10.0 or ir.detectObstacle() == direction_enum.DirectionEnum().FRONT:
                print "Obstacle detected in front"
                mycar.backward()
                mycar.stop()
                time.sleep(0.5)
                nextAction(mycar, ultrasonic)
                time.sleep(0.5)
            elif ir.detectObstacle() == direction_enum.DirectionEnum().LEFT:
                print "Obstacle detected on Left"
                mycar.stop()
                nextAction(mycar, ultrasonic)
                time.sleep(0.5)
            elif ir.detectObstacle() == direction_enum.DirectionEnum().RIGHT:
                print "Obstacle detected on Right"
                mycar.stop()
                nextAction(mycar, ultrasonic)
                time.sleep(0.5)
            else:
                print "No Obstacle detected"
                mycar.forward()
                time.sleep(0.5)
    except KeyboardInterrupt as e:
        print e
    finally:
        mycar.cleanup()


def nextAction(car, sensor):
    ultrasonicservo = servo_ultrasonic.ServoUltraSonic()
    direc = ultrasonicservo.findpath(sensor)
    if direc == direction_enum.DirectionEnum().LEFT:
        car.left()
    elif direc == direction_enum.DirectionEnum().RIGHT:
        car.right()
    elif direc == direction_enum.DirectionEnum().FRONT:
        car.forward()

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s")
    main()
    print "program ends"