import pytest
from jar import Jar


def test_create_jar_default_values():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12



def test_capacity_valueerror_int():
    with pytest.raises(ValueError):
        jar = Jar(capacity=-1)
    with pytest.raises(ValueError):
        jar = Jar(capacity="asd")


def test_adding():
    jar = Jar()
    jar.deposit(8)
    with pytest.raises(ValueError):
        jar.deposit(12)

def test_sub():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(12)
    with pytest.raises(ValueError):
        jar.withdraw(12)

