import unittest
import sys
from basic_integration_test import BasicIntegrationTest
from test_rm_utility import TestRmUtility

def main():
    suite = unittest.TestSuite()
    suite.addTest(
         BasicIntegrationTest.parametrize(
             TestRmUtility)) 
    returnCode = not unittest.TextTestRunner(
        verbosity=2).run(suite).wasSuccessful()
    sys.exit(returnCode)


if __name__ == '__main__':
    main()
