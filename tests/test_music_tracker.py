import pytest 
from lib.music_tracker import *

"""
given an empty string
return an error
"""
def test_given_an_empty_string():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        music_tracker.add("")
    assert str(err.value) == "No music added"
        
        
        
"""
given a string with a song
it will return list with the song added to it
"""
def test_given_song_returns_list_with_song_added():
    music_tracker = MusicTracker()
    music_tracker.add("Rebecca Black - Friday")
    result = music_tracker.song_list
    assert result == ["Rebecca Black - Friday"]
    
"""given more than one song
it will return list with all the songs added"""

def test_without_completed_task():
    music_tracker = MusicTracker()
    music_tracker.add("Rebecca Black - Friday")
    music_tracker.add("Justin Bieber - Baby")
    music_tracker.add("Beyonce - Single Ladies")
    music_tracker.add("Kanye West - All of the lights")
    result = music_tracker.song_list
    assert result == ["Rebecca Black - Friday", "Justin Bieber - Baby", "Beyonce - Single Ladies", "Kanye West - All of the lights"]


"""given the wrong data type
it returns an error message"""

def test_when_given_a_wrong_data_type():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        music_tracker.add(2)
    assert str(err.value) == "No music added"