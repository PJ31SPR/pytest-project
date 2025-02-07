from lib.make_snippet import *

def test_empty_snippet():
    assert make_snippet('') == ''

def test_single_word_string():
    assert make_snippet('hello') == 'hello'

def test_first_five_words():
    assert make_snippet('These are the first five') == 'These are the first five'

def test_over_five_words():
    assert make_snippet('These are the first five words in this string') == 'These are the first five...'