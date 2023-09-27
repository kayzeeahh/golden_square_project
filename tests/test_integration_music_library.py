from lib.music_library import *
from lib.track import *
"""Given I add two tracks
I can see them represented in the list"""

def test_adds_multiple_tracks_and_lists_them():
    music_library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 2")
    track_2 = Track("My Title 2", "My Artist 2")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.all() == [track_1, track_2]
    
    
"""Given I add two tracks
If i search for the title of one of the tracks
I get that track back in the result"""

def test_searches_by_title():
    music_library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 2")
    track_2 = Track("My Title 2", "My Artist 2")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("My Title 2") == [track_2]
    
"""
Given I add two tracks
if I searcg for part of the title
I get the matching track back in the result
"""

def test_searches_by_part_of_title():
    music_library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 2")
    track_2 = Track("My Title 3", "My Artist 4")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("1") == [track_1]
    
