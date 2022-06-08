from jar import Jar
import pytest


def test_init():
    jar = Jar(capacity=10, size=1)
    assert jar.capacity == 10
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar = Jar(capacity=-1)
        jar = Jar(size=1.5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar(size=1)
    jar.withdraw(1)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(5)
