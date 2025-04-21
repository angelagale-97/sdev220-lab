""" 
This code will define two test functions, 
one as a list and the other as a tuple.
"""

def test_sum():
    assert sum([2, 4, 6]) == 12, "Should be 12"

def test_sum_tuple():
    assert sum((2, 3, 6)) == 12, "Should be 12"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")