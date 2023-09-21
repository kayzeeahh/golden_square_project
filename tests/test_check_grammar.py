from lib.check_grammar import *

# Given a lower and an uppercase word
# It returns a list with the uppercase word
def test_check_no_capital_no_punctuation():
    result = check_grammar("this is not correct")
    assert result == False


# Given a capital letter and punctuation
# It returns True"""
def test_check_capital_and_punctuation():
    result = check_grammar("This is now correct.")
    assert result == True
    
    
# Given a capital letter but not punctuation
# It returns close, try again"
def test_capital_no_punctuation():
    result = check_grammar("This is almost correct")
    assert result == "Close, try again!"
    
# Given punctuation but not capital letter
# It returns close, try again"
def test_no_capital_but_punctuation():
    result = check_grammar("this is also almost correct.")
    assert result == "Close, try again!"