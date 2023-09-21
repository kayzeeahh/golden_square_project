def check_grammar(str):
    if str[0].isupper() and str[-1] in [".", "?", "!"]:
        return True
    else:
        if str[0].isupper() and str[-1] not in [".", "?", "!"]:
            return "Close, try again!"
        else:
            if str[0].islower() and str[-1] in [".", "?", "!"]:
                return "Close, try again!"
    return False
    