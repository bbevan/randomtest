import unittest
from randomtest import RandomTest

class randomTestTest(unittest.TestCase):

    def test_True(self):
        True

    def test_object_creation(self):
        myObj = RandomTest()
        self.assertTrue(myObj)

    def test_object_with_constructor(self):
        myObj = RandomTest(12345)
        self.assertTrue(myObj)

    def test_object_without_constructor(self):  
        myObj = RandomTest()
        not myObj.seed

    def test_another_object_without_constructor(self):
        myObj = RandomTest()
        self.assertNotEqual(myObj.seed, 11111111)

    def test_rnglist(self):
        myObj = RandomTest()
        self.assertEqual(myObj.rnglist, [])

    def test_rnglist_list(self):
        myObj = RandomTest(12345678)
        myObj.createRngList()
        self.assertEqual(myObj.rnglist, [0, 1, 1, 0, 1, 0, 1, 1, 1, 1])

if __name__ == 'main':
    unittest.main()