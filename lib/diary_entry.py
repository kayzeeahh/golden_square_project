class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("No title or content provided")
        self.title = title
        self.contents = contents
        
    def format(self,):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        words = self.format().split()
        return len(words)
    
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Error, cannot accept 0 wpm")
        contents_word_count = len(self.contents.split())
        return round(contents_word_count / wpm)
    
    def reading_chunk(self, wpm, minutes):
        readable_chunk = wpm * minutes
        words = self.contents.split()
        chunk_words = words[:readable_chunk]
        return " ".join(chunk_words)
        