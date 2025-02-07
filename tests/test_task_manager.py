
# As a user
# So that I can find my tasks among all my notes
# I want to check if a line from my notes includes the string `#TODO`.

# >>> includes_todo("#TODO buy milk")
# True
# >>> includes_todo("drink tea")
# False
# >>> includes_todo("learn to test-drive my code #TODO")
# True

import pytest
from lib.task_manager import *

"""
Given a string with #TODO, the fn returns the value True
"""
def test_find_to_do_tasks_returns_True_when_match_found():
    assert find_to_do_tasks('#TODO walk dog') == True

"""
Given a string without #TODO, fn returns false
"""
def test_find_to_do_tasks_returns_False_when_no_match():
    assert find_to_do_tasks('walk dog') == False


"""
Given a string with lowercase #todo, fn returns True
"""
def test_find_to_do_tasks_returns_True_when_to_do_is_lowercase():
    assert find_to_do_tasks('#todo walk dog again') == True

"""
Raise an err when text input is empty string
"""
def test_find_to_do_tasks_raises_err_when_empty_string_passed():
    with pytest.raises(Exception) as e:
        find_to_do_tasks('')
    assert str(e.value) == 'Error: function find_to_do_tasks takes an input of string'

"""
Raise an err when input type not string
"""
def test_find_to_do_tasks_raises_err_when_input_not_type_string():
    with pytest.raises(Exception) as e:
        find_to_do_tasks(42)
    assert str(e.value) == 'Error: input must be a string'