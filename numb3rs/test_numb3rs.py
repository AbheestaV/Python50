from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("256.255.255.255") == False
    assert validate("cat") == False
    assert validate("10.10.10.10.10") == False
    assert validate("-1.-1.-1.-1") == False
    assert validate("12.400.400.400") == False