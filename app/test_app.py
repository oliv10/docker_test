import unittest
from app import app as tapp

class app(unittest.TestCase):
        
    def test_getName(self):
        test = tapp("Name", 56)
        self.assertTrue(test.getName() == "Name")

    def test_getAge(self):
        test = tapp("Name", 56)
        self.assertTrue(test.getAge() == 56)