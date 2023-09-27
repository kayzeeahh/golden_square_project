from lib.track import *

"""When we create a new track
we get its title and artist back"""

def test_create_track_and_get_title():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title"
    assert track.artist == "My Artist"
    
def test_format_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track.format() == "My Title by My Artist"