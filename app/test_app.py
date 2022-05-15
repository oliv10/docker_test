import unittest
from app import *

class test_app(unittest.TestCase):
        
    def test_getName(self):
        test = app("Name", 56)
        self.assertTrue(test.getName() == "Name")

    def test_getAge(self):
        test = app("Name", 56)
        self.assertTrue(test.getAge() == 56)

if __name__ == '__main__':
    unittest.main()