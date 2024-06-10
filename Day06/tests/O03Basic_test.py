import math

import pytest
import math

def test_check_sqrt(get_val):
    assert math.sqrt(get_val) == 10

def test_check_divsible_by_4(get_val):
    assert get_val % 4 != 0
