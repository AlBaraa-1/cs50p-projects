import pytest
from datetime import date, datetime
from seasons import parse_date

def test_valid_date():
    # Test parsing a valid ISO date string
    result = parse_date("2000-01-01")
    assert isinstance(result, date)
    assert result == date(2000, 1, 1)

def test_invalid_format():
    # Test parsing an invalid date format (should exit)
    with pytest.raises(SystemExit):
        parse_date("01-01-2000")

def test_non_date_string():
    # Test parsing a non-date string (should exit)
    with pytest.raises(SystemExit):
        parse_date("hello world")

def test_empty_string():
    # Test parsing an empty string (should exit)
    with pytest.raises(SystemExit):
        parse_date("")

def test_leap_year():
    # Test parsing a valid leap year date
    result = parse_date("2020-02-29")
    assert isinstance(result, date)
    assert result == date(2020, 2, 29)