import pytest
from jar import Jar

def test_init_default():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_custom_and_invalid():
    jar = Jar(5)
    assert jar.capacity == 5
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("lots")

def test_str_and_deposit_withdraw():
    jar = Jar(3)
    assert str(jar) == ""        # empty
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪"

def test_deposit_errors():
    jar = Jar(2)
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit(3)            # over capacity

def test_withdraw_errors():
    jar = Jar(2)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw(3)           # more than size
