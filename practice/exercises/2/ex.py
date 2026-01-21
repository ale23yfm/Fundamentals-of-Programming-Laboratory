def function(n):
    """
    The function verifies if a number is prime.
    :param n: a given integer number
    :return: True if n is prime, False otherwise
    """
    d = 2
    while (d < n - 1) and n % d > 0:
        d += 1
    return d >= n - 1