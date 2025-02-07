from lib.count_words import *

def test_count_words_empty_string():
    assert count_words('') == 0

def test_count_words_single_word():
    assert count_words('hello') == 1

def test_count_words_multiple_words():
    assert count_words('Hello hello hello') == 3