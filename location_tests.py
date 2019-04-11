import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("New York", 123.5, 234.4)
        self.assertEqual(repr(loc2),"Location('New York', 123.5, 234.4)")
        loc3 = Location("Oxnard", 143.5, -87.8)
        self.assertEqual(repr(loc3),"Location('Oxnard', 143.5, -87.8)")
    
    # Add more tests!
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.__eq__(loc2), loc == loc2)
        loc3 = Location("New York", 123.5, 234.4)
        loc4 = Location("New York", 123.5, 234.4)
        self.assertEqual(loc3.__eq__(loc4), loc3 == loc4)
        loc5 = Location("Oxnard", 143.5, -87.8)
        loc6 = Location("Oxnard", 143.5, -87.8)
        self.assertEqual(loc5.__eq__(loc6), loc5 == loc6)
        loc7 = Location("Ventura", 167.5, -40.3)
        loc8 = Location("Ventura", 167.5, -40.3)
        self.assertEqual(loc7.__eq__(loc8), loc7 == loc8)

if __name__ == "__main__":
        unittest.main()
