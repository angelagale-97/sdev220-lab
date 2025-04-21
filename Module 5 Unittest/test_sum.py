""" 
This code will define a function to test the sum of a set of numbers.
"""

def test_sum(): 
    assert sum([2, 4, 6]) == 12, "Should be 12"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")