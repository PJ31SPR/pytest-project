import pytest
from lib.ex_one import *

def test_calc_reading_time_no_text():
    with pytest.raises(Exception) as err:
        calc_reading_time(0) 
    err_msg = str(err.value)
    assert err_msg == f"I can't estimate reading time for empty text"

def test_calc_reading_time_200_words():
    assert calc_reading_time(200) == f"It will take approximately 1.0 minutes to read this"

def test_calc_reading_time_not_whole_min():
    assert calc_reading_time(546) == f"It will take approximately 2.73 minutes to read this"

