import unittest


class NewObj:
    def new_method(self, x):
        return x


class NewTest(unittest.TestCase):
    def __init__(self, test_name):
        super(NewTest, self).__init__(test_name)

    def setUp(self):
        self.new_test_instance = NewObj()

    def test_new_method(self):
        self.assertEqual("123", self.new_test_instance.new_method("123"))
