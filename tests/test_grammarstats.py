import pytest 
from lib.grammarstats import *

# Given a lower and an uppercase word
# It returns a list with the uppercase word
def test_check_no_capital_no_punctuation____():
    grammar_stat = GrammarStats()
    result = grammar_stat.check("this is not correct")
    assert result == False


# Given a capital letter and punctuation
# It returns True"""
def test_check_capital_and_punctuation_():
    grammar_stat = GrammarStats()
    result = grammar_stat.check("This is now correct.")
    assert result == True
    
    
# Given two valid sentences
# It returns True
def test_two_sentence():
    grammar_stat = GrammarStats()
    result = grammar_stat.check("This is accurate. So is this.")
    assert result == True
    
# Given that sentence has invalid punctuation
# it returns False

def test_a_mixed_sentence():
    grammar_stat = GrammarStats()
    result = grammar_stat.check("This is right. but this is wrong")
    assert result == False
    
# Given 1 text of 1 text passed
# it returns 100

def test_for_100_percent():
    grammar_stat = GrammarStats()
    grammar_stat.check("This is right.")
    result = grammar_stat.percentage_good()
    assert result == 100
    
# Given 4 text and 2 pass
# it returns 50

def test_for_50_percent():
    grammar_stat = GrammarStats()
    grammar_stat.check("This is right.")
    grammar_stat.check("This is wrong")
    grammar_stat.check("This is right!")
    grammar_stat.check("this is right.")
    result = grammar_stat.percentage_good()
    assert result == 50
    
# Given 0 text 
# it returns an error message

def test_for_no_text():
    grammar_stat = GrammarStats()
    with pytest.raises(Exception) as err:
        grammar_stat()
        assert str(err.value) == "No text given"


    
    