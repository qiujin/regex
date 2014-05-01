from nose2.compat import unittest
from nose2.tools import params

class TestsCanBeUnittestTestCases(unittest.TestCase):
    def setUp(self):
        self.x = 1

    def tearDown(self):
        self.x = None

    def test_can_use_setup_teardown(self):
        print("Test can use setup and teardown")

    def test_can_read_x_value(self):
        print("Test can be unittest testcases")

    @params(1,2,3)
    def test_can_receive_params(self, p):
        print("Test can receive params as a tuple.", p)

