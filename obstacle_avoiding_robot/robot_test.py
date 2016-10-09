#!/usr/bin/python -tt
import sys
import unittest
import robot

class UltrasonicSensorTest(unittest.TestCase):
    # test UltrasonicSensor class
    # before testing, delete all *.pyc

    def setUp(self):
        self.robot = robot.Robot()

    def tearDown(self):
        self.robot.cleanup()

    def test_forward(self):
        self.robot.forward()
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertIn('move forward', output)

    def test_backward(self):
        self.robot.backward()
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertIn('move backward', output)

    def test_left(self):
        self.robot.left()
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertIn('turn left', output)

    def test_right(self):
        self.robot.right()
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertIn('turn right', output)

    def test_stop(self):
        self.robot.forward()
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()  # because stdout is an StringIO instance
        self.assertIn('stop', output)


if __name__ == '__main__':
    assert not hasattr(sys.stdout, "getvalue")
    unittest.main(module=__name__, buffer=True, exit=False)
