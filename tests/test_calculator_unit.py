import pytest
from quick_calc.calculator import Calculator

calc = Calculator()

# --- Basic Operations ---

def test_addition():
    assert calc.add(5, 3) == 8

def test_subtraction():
    assert calc.subtract(10, 4) == 6

def test_multiplication():
    assert calc.multiply(6, 7) == 42

def test_division():
    assert calc.divide(8, 2) == 4

# --- Edge Cases ---

def test_division_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_negative_numbers():
    assert calc.add(-5, -3) == -8

def test_decimal_numbers():
    assert calc.multiply(2.5, 4) == 10.0

def test_large_numbers():
    assert calc.multiply(1_000_000, 3) == 3_000_000

# --- Clear Function ---

def test_clear():
    calc.result = 100
    assert calc.clear() == 0