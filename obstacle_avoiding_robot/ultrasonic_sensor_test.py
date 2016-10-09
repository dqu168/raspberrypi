#!/usr/bin/python -tt
import unittest
import ultrasonic_sensor

class UltrasonicSensorTest(unittest.TestCase):
    # test UltrasonicSensor class
    # before testing, delete all *.pyc

    def setUp(self):
        self.sensor = ultrasonic_sensor.UltrasonicSensor()

    def tearDown(self):
        self.sensor.cleanup()

    def test_measure(self):
        distance = self.sensor.measure()
        print "Distance : %.1f cm" % distance
        print type(distance)
        self.assertTrue(type(distance) is float)

    def test_measure_average(self):
        distance = self.sensor.measure_average()
        print "Avg distance : %.1f cm" % distance
        print type(distance)
        self.assertTrue(type(distance) is float)

if __name__ == '__main__':
    unittest.main()
