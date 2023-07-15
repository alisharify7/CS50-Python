import pytest
import working

def test_valid_time():
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("9:00 AM to 10:00 AM") == "09:00 to 10:00"

def test_value_error():
    with pytest.raises(ValueError):
        working.convert('09:00 AM to 605:00 PM')
        working.convert('05:00 AM 648:00 PM')

    with pytest.raises(ValueError):
        working.convert(" ")
        working.convert(" to ")
        working.convert("9:60 AM to 5:80 PM")