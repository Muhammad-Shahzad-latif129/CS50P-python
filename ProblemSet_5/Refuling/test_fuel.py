import pytest
from fuel import convert, gauge

# Tests for convert
def test_convert_proper_fraction():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("2/5") == 40

def test_convert_zero():
    assert convert("0/4") == 0

def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/4")  

# Tests for gauge
def test_gauge_empty_and_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
