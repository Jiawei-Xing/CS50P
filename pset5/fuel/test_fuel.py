from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("4/5") == 80
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("a/b")


def test_gauge():
    assert gauge(80) == "80%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"