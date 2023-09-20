from lib.fizzbuzz import *

#returns number is not divisible by 3 or 5

def test_not_divisible_by_3_or_5():
    result = fizzbuzz(1)
    assert result == 1
    
#given a number divisible by 3, returns "Fizz"

def test_divible_three():
    result = fizzbuzz(9)
    assert result == "Fizz"
    
#given a number divisible by 3 and 5, returns "Fizzbuzz"
def test_divisible_by_five():
    result = fizzbuzz(10)
    assert result == "Buzz"
    
def test_divisible_by_three_and_five():
    result = fizzbuzz(15)
    assert result == "Fizzbuzz"