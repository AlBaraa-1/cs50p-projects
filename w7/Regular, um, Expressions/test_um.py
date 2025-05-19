from um import count


def test_single_um():
    assert count("um") == 1
    

def test_um_in_sentence():
    assert count("Um, thanks for the album.") == 1

def test_multiple_ums():
    assert count("Um, um, um.") == 3

def test_um_as_substring():
    assert count("yummy") == 0
    assert count("Umum") == 0