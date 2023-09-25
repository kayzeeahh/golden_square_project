class MusicTracker:
    def __init__(self):
        self.song_list = []
        
    def add(self, string):
        if string == "" or type(string) != str:
            raise Exception("No music added")
        self.song_list.append(string)
        
        