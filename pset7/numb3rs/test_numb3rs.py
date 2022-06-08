from numb3rs import validate

def test_letter():
    assert validate("cat.dog.fish.bird") == False

def test_four():
    assert validate("1.2.3") == False

def test_number():
    assert validate("1.2.256.0") == False
    assert validate("1.0.88.250") == True