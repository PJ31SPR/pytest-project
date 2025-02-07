# Test-drive a function with the following design:

# A function called count_words that takes a string as an argument and returns the number of words in that string.

def count_words(string):

    if len(string) == 0:
        return 0
    
    str_arr = string.split()
    return len(str_arr)