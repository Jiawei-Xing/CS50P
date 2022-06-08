from plates import is_valid

def test_correct():
    assert is_valid("JX1997") == True

def test_start():
    assert is_valid("X1997") == False
    assert is_valid("1997") == False

def test_len():
    assert is_valid("JX19970") == False
    assert is_valid("J") == False

def test_number():
    assert is_valid("JJ97XX") == False
    assert is_valid("JX097") == False

def test_punc():
    assert is_valid("JX 97") == False
    assert is_valid("JX97.") == False
    assert is_valid("JX,97") == False