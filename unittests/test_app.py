import unittest
from app import *

class test_app(unittest.TestCase):

    def test_getName(self):
        man = app("Name")
        self.assertTrue(man.getName() == "Name")

if __name__ == '__main__':
    unittest.main()