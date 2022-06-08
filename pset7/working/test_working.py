from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM 10 PM")

def test_valid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 13:00 PM")

def test_correct():
    assert convert("1 PM to 12 AM") == "13:00 to 00:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"