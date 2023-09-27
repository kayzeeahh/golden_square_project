from lib.music_library import *

"""Given no tracks
it returns and empty list"""
    
def test_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []
    
"""
Given no searches
gets an empty list
"""
def test_searches_returns_empthy_list():
    music_library = MusicLibrary()
    assert music_library.search_by_title("Artist 1") == []