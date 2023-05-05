from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
def test_str():
    jar = Jar()
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
def test_deposit2():
    jar = Jar()
    jar.deposit(4)
    jar.deposit(4)
    assert jar.size == 8
def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
def test_error():
    jar = Jar()
    jar.deposit(4)
    with pytest.raises(ValueError):
        jar.withdraw(6)