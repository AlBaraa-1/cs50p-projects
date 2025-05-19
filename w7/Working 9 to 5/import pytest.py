import pytest

from working import convert

def test_convert_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_convert_with_minutes():
    assert convert("9:30 AM to 5:15 PM") == "09:30 to 17:15"
    assert convert("12:05 AM to 12:45 PM") == "00:05 to 12:45"

def test_convert_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM-5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to")
    with pytest.raises(ValueError):
        convert("")

def test_convert_missing_minutes():
    assert convert("1 PM to 2 PM") == "13:00 to 14:00"
    assert convert("12 AM to 1 AM") == "00:00 to 01:00"