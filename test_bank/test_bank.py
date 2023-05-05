from bank import value

def test_value():
    assert value("heLlo") == 0
    assert value("hey") == 20
    assert value("Oh my god") == 100