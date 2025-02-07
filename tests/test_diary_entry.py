import pytest
from lib.diary_entry import *

"""
raises an err for empty str
"""

def test_DiaryEntry_empty_string():
    with pytest.raises(Exception) as err:
        DiaryEntry('','')
    err_msg = str(err.value)
    assert err_msg == 'Entries must have a title and contents'


"""
returns init formatted correctly
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry('My Title', 'some contents')
    assert diary_entry.format() == 'My Title: some contents'

"""
count words returns no. of words in the diary entry
"""

def test_num_of_words_in_title_and_contents():
    diary_entry = DiaryEntry('Title', 'this is the entry')
    assert diary_entry.count_words() == 5

"""
Test reading_time with zero wpm
"""
def test_reading_time_with_zero_wpm():
    diary_entry = DiaryEntry('My Title', 'some contents')
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Reading speed cannot be zero"


"""
test reading time
"""

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry('My Title', 'some contents for the diary')
    assert diary_entry.reading_time(2) == 3.5

def test_reading_time_with_exact_division():
    diary_entry = DiaryEntry("My Title", "one two three four")
    assert diary_entry.reading_time(2) == 3.0  

def test_reading_time_with_single_word():
    diary_entry = DiaryEntry("My Title", "word")
    assert diary_entry.reading_time(2) == 1.5 