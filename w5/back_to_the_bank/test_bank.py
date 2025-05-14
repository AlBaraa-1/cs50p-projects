from bank import value

def test_hello_variants():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("   hello") == 0
    assert value("hello123") == 0

def test_h_variants():
    assert value("h") == 20
    assert value("H") == 20
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("   h") == 20
    assert value("   hi123") == 20

def test_random_words():
    assert value("wassup") == 100
    assert value("hey") == 20  # starts with 'h' → $20
    assert value("yo") == 100
    assert value("  yo") == 100
