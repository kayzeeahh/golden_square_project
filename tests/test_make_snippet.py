from lib.make_snippet import *

# returns a string of only 5 words

def test_string_is_exactly_5_words():
    result = make_snippet("there are five words here")
    assert result == "there are five words here"
    
#returns the first 5 words of a string longer than 5

def test_string_is_over_5_words():
    result = make_snippet("There are way more than 5 words here")
    assert result == "There are way more than..."
    
#returns less than 5 words
def test_string_is_less_than_5_words():
    result = make_snippet("there are words here")
    