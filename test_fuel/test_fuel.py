from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"

def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")