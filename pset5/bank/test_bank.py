from bank import value

def test_hello():
    assert value("hello!") == 0
    assert value("Hello!") == 0

def test_h():
    assert value("hi!") == 20
    assert value("Hi!") == 20

def test_other():
    assert value("Good morning!") == 100
