
import pytest
from simple_math import (
    simple_add,
    simple_sub,
    simple_mult,
    simple_div,
    poly_first,
    poly_second
)

# ----------------------
# simple_add
# ----------------------
@pytest.mark.parametrize("a,b,expected", [
    (1, 0, 1),
    (1, 1, 2),
    (1, 2, 3),
])
def test_simple_add(a, b, expected):
    assert simple_add(a, b) == expected


# ----------------------
# simple_sub
# ----------------------
@pytest.mark.parametrize("a,b,expected", [
    (1, 0, 1),
    (2, 1, 1),
    (1, 2, -1),
])
def test_simple_sub(a, b, expected):
    assert simple_sub(a, b) == expected


# ----------------------
# simple_mult
# ----------------------
@pytest.mark.parametrize("a,b,expected", [
    (1, 0, 0),
    (2, 3, 6),
    (-1, 3, -3),
])
def test_simple_mult(a, b, expected):
    assert simple_mult(a, b) == expected


# ----------------------
# simple_div
# ----------------------
@pytest.mark.parametrize("a,b,expected", [
    (2, 1, 2),
    (6, 3, 2),
])
def test_simple_div(a, b, expected):
    assert simple_div(a, b) == expected


def test_simple_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        simple_div(1, 0)


# ----------------------
# poly_first
# f(x) = a0 + a1*x
# ----------------------
@pytest.mark.parametrize("x,a0,a1,expected", [
    (1, 1, 1, 2),
    (2, 0, 3, 6),
    (3, 1, 2, 7),
])
def test_poly_first(x, a0, a1, expected):
    assert poly_first(x, a0, a1) == expected


# ----------------------
# poly_second
# f(x) = a0 + a1*x + a2*x^2
# ----------------------
@pytest.mark.parametrize("x,a0,a1,a2,expected", [
    (1, 1, 1, 1, 3),
    (2, 0, 1, 1, 6),
    (3, 1, 0, 1, 10),
])
def test_poly_second(x, a0, a1, a2, expected):
    assert poly_second(x, a0, a1, a2) == expected
