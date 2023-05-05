from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True

def test_zero_check():
    assert is_valid("CS05") == False

def test_char_check():
    assert is_valid("PI3.14") == False

def test_small_check():
    assert is_valid("H") == False

def test_num_check():
    assert is_valid("OUTATIME") == False

def test_num2_check():
    assert is_valid("OUT32E") == False

def test_alpha_check():
    assert is_valid("4444") == False

