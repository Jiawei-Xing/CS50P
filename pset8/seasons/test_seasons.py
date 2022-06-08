from seasons import delta, words
from datetime import date

def test_minutes():
    d = date.fromisoformat('1997-04-23')
    timedelta = date.today() - d
    assert delta(d) == timedelta.days * 24 * 60

def test_words():
    assert words(525600) == "five hundred and twenty-five thousand, six hundred"