from seasons import convert
import pytest

def test_convert():
    assert convert("2020-10-10") == "One million, three hundred forty-four thousand, nine hundred sixty minutes"
    assert convert("2022-02-06") == "Six hundred forty-eight thousand minutes"
    with pytest.raises(SystemExit):
        convert("5555-25-29")
