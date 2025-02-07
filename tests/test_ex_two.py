import pytest
from lib.ex_two import *

"""
fn signature
def grammar_check(text):
- verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

parameters: string of text

return: msg indicating pass or fail, string

side effects: 
"""
#=================================================================#
"""
test_err_msg_returned_when_empty_string_passed
"""

def test_grammar_check_empty_str():
    with pytest.raises(Exception) as err:
        grammar_check('')
    err_msg = str(err.value)
    err_msg = "I can't check an empty sentence"
    
"""
test_string_starts_with_capital
"""

def test_grammar_check_starts_with_capital():
    assert grammar_check('Hello there?') == True

"""
test_string_ends_with_correct_punctuation
"""

def test_grammar_check_ends_with_punctuation():
    assert grammar_check('Hello there!') == True
"""
test_fail_msg_returned_when_string_fails_punctuation_criteria
"""

def test_grammar_check_returns_fail_when_it_fails():
    assert grammar_check('Hello there') == False
"""
tests that fail msg returned when capital missing
"""

def test_grammar_check_returns_fail_when_it_fails_on_capital():
    assert grammar_check('hello there!') == False