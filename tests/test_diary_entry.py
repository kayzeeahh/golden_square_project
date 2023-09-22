import pytest
from lib.diary_entry import *

# When given a tile and content
# return the title and content

def test_for_format():
    diary_entry = DiaryEntry("Harry Potter", "contents")
    result = diary_entry.format()
    assert result  == "Harry Potter: contents"
    
# When given the title and contents
# returns the title and content and counts of words

def test_for_count_words():
    diary_entry = DiaryEntry("Harry Potter", "contents")
    result = diary_entry.count_words()
    assert result == 3
    
# when given an empty title and contents
# raises and error

def test_on_empty_title_and_contents_error():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "")
    assert str(err.value) == "No title or content provided"
    
# When given the a reading time of 2
# returns 1

def test_reading_time_with_two_wpm():
    diary_entry = DiaryEntry("Harry Potter", "one two")
    result = diary_entry.reading_time(2)
    assert result == 1


# when given the reading time of 2 wpm
# returns 4 words

def test_reading_time_two_wpm_returns_four():
    diary_entry = DiaryEntry("Harry Potter", "one to three four")
    result = diary_entry.reading_time(2)
    assert result == 2
    
# when given a wpm of 2
# with a text of 3 words
# returns 1.5

def test_reading_time_2wpm_returns_float():
    diary_entry = DiaryEntry("Harry Potter", "one two three")
    result = diary_entry.reading_time(2)
    assert result == 2
    
def test_reading_time_error():
    diary_entry = DiaryEntry("Harry Potter", "one two three")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Error, cannot accept 0 wpm"
    
# Given content of 6 words 
# and wpm of 2
# and 2 mins
# return 4 words

def test_for_4_words():
    diary_entry = DiaryEntry("Harry Potter", "one two three four five six")
    result = diary_entry.reading_chunk(2,2)
    assert result == "one two three four"
    
    
# Given of 6 words 
# and a wpm of 2
# and 3 mins
# return 6 words
def test_for_6_words():
    diary_entry = DiaryEntry("Harry Potter", "one two three four five six")
    result = diary_entry.reading_chunk(2,3)
    assert result == "one two three four five six"