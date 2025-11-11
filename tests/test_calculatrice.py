from calculatrice import Calculatrice
import pytest

@pytest.mark.parametrize("a, b, attendu", [
    (1, 1, 2),
    (2, -2, 0),
    (-3, -4, -7)
])
def test_addition_parametree(a, b, attendu):
    calc = Calculatrice()
    assert calc.addition(a, b) == attendu

def test_division_normale():
    calc = Calculatrice()
    assert calc.division(10, 2) == 5

def test_division_par_zero():
    calc = Calculatrice()
    with pytest.raises(ValueError):
        calc.division(5, 0)
