"""
Compute the sum of even elements in the given list input:
l - the list of numbers

output:
The sum of the even elements in the list

Raises TypeError if parameter l is not a Python list
Raises ValueError if the list does not contain even numbers
"""

def sum_even(l):
    sum = 0
    if not isinstance(l, list):
        raise TypeError("The list must be a Python list.")
    for num in l:
        if num %2 == 0:
            sum += num
    if sum == 0:
        raise ValueError("The list does not contain even numbers.")
    return sum

