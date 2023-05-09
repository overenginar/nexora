import unittest

from .test_dummy import NewTest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    test_names = loader.getTestCaseNames(NewTest)

    for test_name in test_names:
        suite.addTest(NewTest(test_name))

    unittest.TextTestRunner(verbosity=2).run(suite)
