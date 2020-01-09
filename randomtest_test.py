import unittest
from randomtest import RandomTest

defaultrnglist = [1, 1, 0, 1, 1, 0, 1, 0, 0, 1]

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
        self.assertEqual(myObj.rnglist, defaultrnglist)

    def test_rnglist_list(self):
        myObj = RandomTest(12345678)
        myObj.createRngList()
        self.assertEqual(myObj.rnglist, [0, 1, 1, 0, 1, 0, 1, 1, 1, 1])

    def test_default_seed(self):
        myObj = RandomTest()
        myObj.createRngList()
        self.assertEqual(myObj.defaultseed, 123456789123456789)

    # test if the default seed creates the rnglist on init
    def test_default_rnglist_init(self):
        myObj = RandomTest()
        self.assertEqual(myObj.rnglist, defaultrnglist)

    # test that only the constructor can create the rng list
    # what the hell is this test?
    def test_constructor_rnglist_only(self):
        myObj = RandomTest()
        myObj.createRngList()
        # should return true because the list is no longer than 9,10 
        # elements.
        self.assertEqual(myObj.rnglist, defaultrnglist)


 
if __name__ == 'main':
    unittest.main()