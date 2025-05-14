from plates import is_valid

def test_start_with_atleast_2_letters():
    assert is_valid("12hell") == False
    assert is_valid("AB123") == True

def test_maximum_length():
    assert is_valid("hello123") == False

def test_minimum_length():
    assert is_valid("h") == False

def test_middle_numbers():
    assert is_valid("AAA22A") == False

def test_no_spcial_char():
    assert is_valid("hi@123") == False

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("AB123") == True
    assert is_valid("HELLO") == True

def test_no_leading_zero():
    assert is_valid("CS01") == False

def test_numbers_must_be_terminal():
    assert is_valid("C5S0") == False
    
def test_all_digits():
    assert is_valid("123456") == False
    assert is_valid("1234") == False