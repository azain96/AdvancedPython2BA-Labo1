# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils
from math import sqrt

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(4), 24)
        self.assertEqual(utils.fact(5), 120)
        self.assertEqual(utils.fact(1), 1)
        self.assertEqual(utils.fact(0), 1)
        
    
    def test_roots(self):
        self.assertEqual(utils.roots(1, 4, 6), ())
        self.assertEqual(utils.roots(1, 4, 4), (-2))
        self.assertEqual(utils.roots(1, 8, 12), (-2,-6))
            
        
    
    def test_integrate(self):
        self.assertEqual(utils.integrate('3*x ** 2 - 1', 0, 1), (0))
        self.assertEqual(utils.integrate('2*x', 0, 1 ), (1))
        self.assertEqual(utils.integrate('4*x ** 3',0 ,1),(1))
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
