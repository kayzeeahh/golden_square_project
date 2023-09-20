def e_extractor(str):
    if "e" in str:
        #letter_es = [letter for letter in str if letter == 'e']
        #non_letter_es = [letter for letter in str if letter != 'e']
        #letters = letter_es + non_letter_es
        #return "".join(letters)
        new_str = ""
        for letter in str:
            if letter == 'e':
                new_str = 'e' + new_str
            else:
                new_str = new_str + letter
        return new_str
    else:
        return str
