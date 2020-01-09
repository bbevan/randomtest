import randomtest
import random
import unittest
from randomtest import RandomTest

class TestRandomTestResultsMethod(unittest.TestCase):

    def test_results(self):
        # non-random function
        x = lambda a,b: a+b
        result = 2
        myObj = RandomTest()
        myObj.randomtest_True(x(1,1), result)

    def test_two_results(self):
        # random function
        x = lambda x: random.randint(0,x)
        results =[0,1]
        myObj = RandomTest()
        myObj.randomtest_True(x(1), results)

    def test_multiple_results(self):
        # another random function
        x = lambda x: random.randint(0,x)
        results = [0,1,2,3,4,5,6,7,8,9,10]
        myObj = RandomTest()
        myObj.randomtest_True(x(10), results)

if __name__=='main':
    unittest.main()
