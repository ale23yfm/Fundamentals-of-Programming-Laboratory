def function(l):
    """
    the function takes a list and verifies if there is at least one even number
    :param l: given list of integers
    :return: TRue if there is at least one even number, False otherwise
    """
    if (l == None):
        raise ValueError
    for e in l:
        if e%2==0:
            return True
    return False