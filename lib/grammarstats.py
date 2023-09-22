class GrammarStats:
    def __init__(self):
        self.total_check = 0
        self.passed = 0
        pass
    
    def check(self, text):
        self.total_check += 1
        if text == "":
            raise Exception("No text given")
        if text[0].isupper() and text[-1] in [".", "?", "!"]:
            self.passed += 1
            return True
        else:
            return False
    
    def percentage_good(self):
        return (self.passed / self.total_check) * 100
