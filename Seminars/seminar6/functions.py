def sinus (x, no_of_iterations):
    """
    function that computes an approximation of the sine of x using Taylor Series
    :param x: float
    :param no_of_iterations: int, >0
    :return: sine of x, float
    """
    s = 0
    t = x
    for i in range(no_of_iterations):
        s += t
        t *= -1 *x*x / ((2*(i+1))*(2*(i+1)+1))
    return s

def cosinus (x, no_of_iterations):
    """
    function that computes an approximation of the cosine of x using Taylor Series
    :param x: float
    :param no_of_iterations: int, >0
    :return: cosine of x, float
    """
    s = 0
    t = 1
    for i in range(no_of_iterations):
        s += t
        t *= -1 * x * x / (2 * i + 1) * (2 * i + 2)
    return s
