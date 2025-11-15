from math import sin, cos
from functions import sinus
from functions import cosinus
from polinomials import create_polinomial, get_degree, get_coefficients

def test_trigonometric_function(maths_function, proposed_function):
    x = 3.14
    no_of_steps = 10
    epsilon = 0.000001
    expected_Result = maths_function(x)
    obtained_Result = proposed_function(x, no_of_steps)
    assert abs(obtained_Result) - abs(expected_Result) < epsilon

def test_polinomials():
    degree = 3
    coefficients = [1, -2, 0, 7]
    #P(x)= 1-2x+7x^3
    polinomial=create_polinomial(degree, coefficients)
    create_polinomial(degree, coefficients)
    assert degree == get_degree(polinomial)
    assert coefficients == get_coefficients(polinomial)

def run_all_tests():
    test_trigonometric_function(sin, sinus)
    test_trigonometric_function(cos, cosinus)
    test_polinomials()