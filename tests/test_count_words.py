from lib.count_words import *

# return 5 when string is 5 words

def test_5_words_in_string():
    result = count_words("there are five words here")
    assert result == 5
    
# returns 0 when string in empty

def test_0_when_string_is_empty():
    result = count_words('')
    assert result == 0