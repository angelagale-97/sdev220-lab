""" 
This code will execute two simple tests that will define methods  
to test a list of integers and test a list of fractions.
"""
from fractions import Fraction

import unittest 

from my_sum import sum 

class TestSum(unittest.TestCase): 
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [2, 4, 6]
        result = sum(data)
        self.assertEqual(result, 12)

    def test_list_fraction(self): 
        """ 
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 3), Fraction(1, 4), Fraction(1, 2)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()