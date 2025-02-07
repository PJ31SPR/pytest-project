import pytest
from lib.grammar_stats_challenge import * 

"""
test instance of class created
"""

def test_GrammarStats_instance_of_class_created_on_init():
    grammar_stats = GrammarStats()
    assert isinstance(grammar_stats, GrammarStats)

"""
test GrammarStats initialises correctly
"""

def test_GrammarStats_init():
    grammar_stats = GrammarStats()
    assert grammar_stats.total_texts == 0
    assert grammar_stats.good_texts == 0

"""
Test check() method for correct sentences
"""
def test_check_good_sentences():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("This is a correct sentence.") == True
    assert grammar_stats.check("Is this good?") == True
    assert grammar_stats.check("Wow!") == True

"""
Test check() method for incorrect sentences
"""
def test_check_bad_sentences():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("this is incorrect.") == False  # No capital letter
    assert grammar_stats.check("This is incorrect") == False   # No punctuation
    assert grammar_stats.check("no punctuation or capitalization") == False

"""
Test check() raises exception for empty string
"""
def test_check_raises_exception_on_empty_string():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception, match="I can't check an empty sentence"):
        grammar_stats.check("")

"""
Test percentage_good() after checking some texts
"""
def test_percentage_good():
    grammar_stats = GrammarStats()
    
    # 2 good, 2 bad
    grammar_stats.check("Correct sentence.")  # Good
    grammar_stats.check("Another good one!")  # Good
    grammar_stats.check("bad sentence")       # Bad
    grammar_stats.check("this one is bad.")   # Bad

    assert grammar_stats.percentage_good() == 50  # 2/4 = 50%
    
    # Add another bad sentence, making it 2/5
    grammar_stats.check("Another bad")
    assert grammar_stats.percentage_good() == 40  # 2/5 = 40%