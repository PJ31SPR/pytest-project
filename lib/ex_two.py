# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

def grammar_check(text):
    if len(text) == 0:
        raise Exception(f"I can't check an empty sentence")
    
    if text[0].islower():
        return False
    
    if text[-1] not in '!?.':
        return False
    
    if text[0].isupper() and text[-1] in '!?.':
        return True