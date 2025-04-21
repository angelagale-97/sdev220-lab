""" 
This code will first import unittest from the library, 
create a class to inherit from TestCase, convert functions to methods,
use the assertEqual() method, and finally change the entry point to unittest.main().
"""

import unittest

class TestSum(unittest.TestCase): 

    def test_sum(self): 
        self.assertEqual(sum([2, 4, 6]), 12, "Should be 12")

    def test_sum_tuple(self): 
        self.assertEqual(sum((2, 3, 6)), 12, "Should be 12")

if __name__ == "__main__":
    unittest.main()