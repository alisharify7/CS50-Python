import pytest
import datetime
from seasons import HumanLiveTime, is_valid_birth_date




def test_invalid_date():
    assert is_valid_birth_date("1954 21") == False
    assert is_valid_birth_date("Sep 10,, 1990") == False
    assert is_valid_birth_date(" 190.10.10") == False
    assert is_valid_birth_date(" 1a0-0-10") == False
    assert is_valid_birth_date("1asd0-1-1") == False



def test_valid_date():
    assert is_valid_birth_date("2000-12-12") != False
    assert is_valid_birth_date("1900-01-08") != False
    assert is_valid_birth_date("2000-01-30") != False


def test_ok():
    date_valid = is_valid_birth_date("1999-01-01")
    date=datetime.date(2000,1,1)
    human = HumanLiveTime(date)

    assert human.calculate(date_valid) == "Five hundred twenty-five thousand, six hundred minutes"
    