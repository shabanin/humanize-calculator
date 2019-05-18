import pytest
from humanize_calculator import int_to_text


def test_int_to_text_type():
    assert type(int_to_text(100)) is str


def test_int_to_text_0():
    assert int_to_text(0) == "zero"


def test_int_to_text_1to19():
    assert int_to_text(12) == "twelve"


def test_int_to_text_0x0():
    assert int_to_text(40) == "forty"


def test_int_to_text_0xx():
    assert int_to_text(72) == "seventy two"


def test_int_to_text_x00():
    assert int_to_text(400) == "four hundreds"


def test_int_to_text_xxx():
    assert int_to_text(125) == "one hundred twenty five"


def test_int_to_text_xxxxx():
    assert int_to_text(12345) == "twelve thousands three hundreds forty five"


def test_int_to_text_too_big():
    assert int_to_text(1000000000000000009) == "999+ quadrillions+"


def test_int_to_text_negative_number():
    assert int_to_text(-1) == "invalid number"


def test_int_to_text_not_int():
    assert int_to_text("364") == "invalid number"


def test_int_to_text_wrong_input():
    assert int_to_text(-1) == "invalid number"


def test_int_to_text_9999999999():
    assert int_to_text(9999999999) == "nine billions nine hundreds ninety nine millions nine hundreds ninety nine thousands nine hundreds ninety nine"

