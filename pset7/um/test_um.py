from um import count

def test_word():
    assert count("Um, thanks for the album.") == 1

def test_space():
    assert count("Um, thanks, um ...") == 2

def test_case():
    assert count("UM um Um uM") == 4