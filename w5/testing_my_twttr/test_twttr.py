from twttr_bugged import shorten


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_shorten_with_spaces():
    assert shorten("hello world") == "hll wrld"
    assert shorten("  hello  ") == "  hll  "


def test_shorten_with_numbers():
    assert shorten("hello123") == "hll123"
    assert shorten("123hello") == "123hll"


def test_shorten_with_voiles():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("aeiou123") == "123"
    assert shorten("123AEIOU") == "123"
