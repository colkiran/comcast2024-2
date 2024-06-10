import pytest

glbX = 100
# @pytest.mark.num
def test_greater():
    n = 10
    assert n < glbX

# @pytest.mark.num
def test_equal():
    n = 100
    assert n >= glbX

# @pytest.mark.num
def test_less():
    n = 500
    assert n < glbX

# @pytest.mark.text
def test_equal_ascii():
    assert "a" == "a"

# @pytest.mark.text
def test_equal_caps():
    assert "Z" == "Z"

# @pytest.mark.text
def test_equal_special():
    assert "*" == "*"
