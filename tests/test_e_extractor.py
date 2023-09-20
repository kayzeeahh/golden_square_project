import pytest
from lib.e_extractor import *

# Return string without any "e" in it

def test_given_to_no_e_return_same():
    result = e_extractor("buiasdkjfdsjnv")
    assert result == "buiasdkjfdsjnv"
    
# returns an empty string

def test_given_an_empty_string():
    result = e_extractor("")
    assert result == ""
    
# extracts an e from string

def test_extracting_an_e_to_the_front():
    result = e_extractor("hey")
    assert result == "ehy"
    
# extracting multiple e from string

def test_extracting_multiple_e_to_the_front():
    result =e_extractor("heloeeooe")
    assert result == "eeeehlooo"
    
# all e already at the start of string

def test_given_e_already_at_the_front():
    result = e_extractor("eeeehlooo")
    assert result == "eeeehlooo"