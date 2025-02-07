## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
# As a user
# So that I can find my tasks among all my notes
# I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def find_to_do_tasks(text):
    """Return any relevant notes with the string '#TODO'

    Parameters: (list all parameters and their types)
        text, string

    Returns: (state the return value and its type)
        True/False, boolean 

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string with #TODO, the fn returns the value True
"""
def test_find_to_do_tasks_returns_True_when_match_found():


"""
Given a string without #TODO, fn returns false
"""
def test_find_to_do_tasks_returns_False_when_no_match():

"""
Given a string with lowercase #todo, fn returns True
"""
def test_find_to_do_tasks_returns_True_when_to_do_is_lowercase():

"""
Raise an err when text input is empty string
"""
def test_find_to_do_tasks_raises_err_when_empty_string_passed():

"""
Raise an err when input type not string
"""
def test_find_to_do_tasks_raises_err_when_input_not_type_string():

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them! -->
