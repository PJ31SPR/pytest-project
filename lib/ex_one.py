# One
# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

def calc_reading_time(words):
    """
    parameters: (number of words, int)

    returns: an estimated time in minutes, float

    side effects: it will return a value, it does nothing else
    """

    if words == 0:
        # return "It will take approximately 0 minutes to read this"
        raise Exception("I can't estimate reading time for empty text")
    time = words / 200 #one / = float, // = normal div

    return f"It will take approximately {time} minutes to read this"