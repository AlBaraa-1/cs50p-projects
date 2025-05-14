from fuel import convert, gauge
import pytest

# --- convert() tests ---


def test_convert_normal():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25


def test_convert_extremes():
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("100/100") == 100


def test_convert_zero():
    assert convert("0/100") == 0


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_numerator_greater():
    with pytest.raises(ValueError):
        convert("5/4")


# --- gauge() tests ---


def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(88) == "88%"
