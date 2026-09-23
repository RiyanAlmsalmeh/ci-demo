import pytest
from calculator import add, divide, subtract, multiply


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


# --- New Tests for subtract ---

def test_subtract_positive():
    assert subtract(5, 3) == 2


def test_subtract_negative():
    assert subtract(-5, -2) == -3


def test_subtract_zero():
    assert subtract(5, 0) == 5


# --- New Tests for multiply ---

def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_negative():
    assert multiply(-2, 4) == -8


def test_multiply_zero():
    assert multiply(5, 0) == 0
