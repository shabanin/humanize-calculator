import pytest
from humanize_calculator import humanize


def test_humanize_type():
    assert type(humanize("0")) is str


def test_humanize_number():
    assert humanize("122") == "one hundred twenty two"


def test_humanize_common():
    assert humanize("1 + 1 = 2") == "one plus one equals two"


def test_humanize_symbols():
    assert humanize("1+=") == "invalid input"


def test_humanize_wrong_symbols():
    assert humanize(" ^ . ") == "invalid input"


def test_humanize_common2():
    assert humanize("1 * 1 = 20 - 19") == "one multiply by one equals twenty minus nineteen"


def test_humanize_spaces():
    assert humanize("      1 * 1 =    20 -    1 9       ") == "one multiply by one equals twenty minus nineteen"


def test_humanize_long():
    assert humanize("1 + 2 - 3 + 4 - 5 = 6 * 7 / 8") == "one plus two minus three plus four minus five equals six multiply by seven divide by eight"
