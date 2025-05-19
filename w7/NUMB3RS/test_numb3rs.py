from numb3rs import validate

def test_valid_ips():
    assert validate("0.0.0.0")
    assert validate("255.255.255.255")
    assert validate("1.2.3.4")
    assert validate("192.168.1.1")
    assert validate("10.0.10.1")

def test_invalid_ips():
    assert not validate("256.100.100.100")
    assert not validate("192.168.1")
    assert not validate("192.168.1.1.1")
    assert not validate("123.456.78.90")
    assert not validate("abc.def.ghi.jkl")
    assert not validate("192.168..1")
