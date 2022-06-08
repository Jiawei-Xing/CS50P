from twttr import shorten

def test_uppercase():
    assert shorten("1 APPLE IS OURS.") == "1 PPL S RS."

def test_lowercase():
    assert shorten("1 apple is ours.") == "1 ppl s rs."