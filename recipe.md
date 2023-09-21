
1. Describe the Problem
# Put or write the user story here. Add any clarifying notes you might have.

> As a user
> So that I can manage my time
>I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute

2. Design the Function Signature
# Include the name of the function, its parameters, return value, and side effects.
def manage_reading_time(words_in_books):
        takes the number of words in a book.
    Parameters: (list all parameters and their type)
        words_in_books: a list of float showung the number of words in multiple book eg. [650, 800, 1500]

    Returns: (state the return value and its type)
        a list of int divided by 200 to show how many mins it takes to read the text

    Side effects: (state any side effects)
        this function must round up to the nearest whole number


    """
3. Create Examples as Tests
# Make a list of examples of what the function will take and return.
'''given a number that is exactly 200
it returns 1 min'''
manage_reading_time(200) >> [1.0]

'''given a number that is less than 200
it returns a decimal number''
manage_reading_time(50) >> [0.25]

'''given a number more than 200
it returns the number divided by 200 rounded up'''
manage_reading_time(450) >> [2.0]

'''given 0, 
it returns 0'''
manage_reading_time(0) >> [0]

'''given a number with a decimal 
it returns the number rounded up and then divided by 200'''
manage_reading_time(200.8) >> [1.0]

'''given a None value
it returns an error'''
manage_reading_time(None) >> error

4. Implement the Behaviour
# After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
 from lib.manage_reading_time import *

'''given a number that is exactly 200
it returns 1 min'''

def test_manage_reading_time(int):
    result = manage_reading_time(200)
    assert result == [1]



