from lib.manage_reading_time import *

# given a number that is exactly 200
# it returns 1 min

def test_for_exactly_200_words():
    result = manage_reading_time(200)
    assert result == 1.0
    
    
# given a number that is less than 200
# it returns a decimal number

def test_manage_reading_time_less_than_200():
    result = manage_reading_time(50)
    assert result == 0.25
    
    
# given 0, 
# it returns 0
def test_when_given_0_or_None_return_error():
    result = manage_reading_time(0)
    assert result == 'Error, no text number given'