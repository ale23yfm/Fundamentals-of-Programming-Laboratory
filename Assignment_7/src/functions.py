#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#

from typing import List, Dict
import random

valid_types = ["water", "heating", "electricity", "gas", "other"]

def save_state(expenses:List[Dict], history:List[Dict]):
    """
    Function to save the HISTORY of expenses.

    Args:
        history: list of dictionaries, last version of "expenses"
        expenses: list of dictionaries
    """

    copied_state = []
    for e in expenses:
        copied_state.append(e.copy())  # copy each dict
    history.append(copied_state)

#A
def add_expense(expenses: List[Dict], history: List[List[Dict]], apartment: int, expense_type: str, amount: int):
    """
    Adds an expense to the list of expenses.

    Args:
        expenses: the list dictionaries representing apartments' expenses
        history: a list of dictionaries representing the previous version of expenses.
        apartment: positive integer
        expense_type: string from the valid_types
        amount: positive integer

    Raises:
        ValueError: if apartment's number is negative integer or non-integer, expense-type is invalid, amount is a negative integer or non-integer
    """

    #saves the current list to be able to undo a change if needed
    save_state(expenses, history)

    if not isinstance(apartment, int) or apartment <= 0:
        raise ValueError("apartment must be a positive integer")
    if expense_type not in valid_types:
        raise ValueError("expense_type must be one of the following: water, heating, electricity, gas and other")
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("amount must be a positive integer")

    expenses.append({
        "apartment": apartment,
        "type": expense_type,
        "amount": amount
    })

#B
def remove_apartment(expenses: List[Dict], history: List[Dict], apartment: int):
    """
    Removes apartment's expenses.

    Args:
        expenses: the list dictionaries representing apartments' expenses
        history: a list of dictionaries representing the previous version of expenses.
        apartment: apartment's number which should be removed

    Raises:
        ValueError: if apartment's number is negative integer or non-integer
    """
    save_state(expenses, history)
    if not isinstance(apartment, int) or apartment <= 0:
        raise ValueError("apartment must be a positive integer.")

    result = []
    for e in expenses:
        if e["apartment"] != apartment:
            result.append(e)

    expenses[:] = result

def remove_apartments_range(expenses: List[Dict], history: List[Dict], start:int, end:int):
    """
    Removes apartment's range.

    Args:
        expenses: the list dictionaries representing apartments' expenses
        history: a list of dictionaries representing the previous version of expenses.
        start: the number of the first apartment in range
        end: the number of the last apartment in range

    Raises:
        ValueError: if apartment's number is negative integer or non-integer
    """

    save_state(expenses, history)
    if not isinstance(start, int) or start <= 0:
        raise ValueError("First apartment must be a positive integer.")
    if not isinstance(end, int) or end <= 0:
        raise ValueError("Last apartment must be a positive integer.")

    result = []
    for e in expenses:
        if not (start <= e["apartment"] <= end):
            result.append(e)

    expenses[:] = result

def remove_type(expenses: List[Dict], history: List[Dict], expense_type: str):
    """
    Removes apartment's expenses.

    Args:
        expenses: the list dictionaries representing apartments' expenses
        history: a list of dictionaries representing the previous version of expenses.
        expense_type: string from the valid_types

    Raises:
        ValueError: if expense-type is invalid
    """

    save_state(expenses, history)
    if expense_type not in valid_types:
        raise ValueError("expense_type must be one of the following: water, heating, electricity, gas and other")

    result = []
    for e in expenses:
        if e["type"] != expense_type:
            result.append(e)

    expenses[:] = result

def replace_amount(expenses: List[Dict], history: List[Dict], apartment: int, expense_type:str, amount: int):
    """
    Replaces apartment's expenses.

    Args:
        expenses: the list dictionaries representing apartments' expenses
        history: a list of dictionaries representing the previous version of expenses.
        apartment: apartment's number which should be removed
        expense_type: string from the valid_types
        amount: positive integer

    Raises:
        ValueError: if apartment's number is negative integer or non-integer, expense-type is invalid, amount is a negative integer or non-integer
    """
    save_state(expenses, history)
    if not isinstance(apartment, int) or apartment <= 0:
        raise ValueError("apartment must be a positive integer.")
    if expense_type not in valid_types:
        raise ValueError("expense_type must be one of the following: water, heating, electricity, gas and other")
    if not isinstance(amount, int) or amount <= 0:
        raise ValueError("amount must be a positive integer")

    for e in expenses:
        if e["apartment"] == apartment and e["type"] == expense_type:
            e["amount"] = amount

#C & D
def filtered_by_amount(expenses: List[Dict], operator: List[Dict], amount:int):
    """
    Gives the dictionaries which respects the given affirmation.

    Examples:
        for operator = "=" and amount = 100 it gives only the expenses with amount equal to 100
        for operator = ">" and amount = 100 it gives only the expenses with amount grater than 100
        for operator = "<" and amount = 100 it gives only the expenses with amount less than 100
    Args:
        expenses: the list dictionaries representing apartments' expenses
        operator: <, =, >
        amount: positive integer

    Returns: the new list of dictionaries representing apartments' expenses, compared to the amount specified.
    """
    result =[]
    for e in expenses:
        if operator == "=" and amount == e["amount"]:
            result.append(e)
        elif operator == "<" and e["amount"] < amount:
            result.append(e)
        elif operator == ">" and e["amount"] > amount:
            result.append(e)
    return result

#D
def filtered_by_type(expenses: List[Dict], expense_type: List[Dict]):
    """
    Filters the expenses according to the specified type.

    Args:
        expenses: the list dictionaries representing apartments' expenses
        expense_type: string from the valid_types

    Returns: the new list of dictionaries representing apartments' expenses, excluding the ones which does not contain the specified type.
    """
    result =[]
    for e in expenses:
        if expense_type == e["type"]:
            result.append(e)

    return result

#E
def undo(expenses: List[Dict], history: List[Dict]):
    """
    Function to undo the last change in the list of expenses.

    Args:
        expenses: the list dictionaries representing apartments' expenses
        history: a list of dictionaries representing the previous version of expenses.
    """
    last_state = history.pop()
    expenses.clear()
    for e in last_state:
        expenses.append(e)

def generate_random_expenses(n: int = 10):
    """
    Function to generate 10 random expenses.

    Args:
        n: number of expenses to generate

    Returns: the dictionary with 10 random expenses
    """

    expenses = []
    for i in range(n):
        expenses.append({
            "apartment": random.randint(1, 100),
            "type": random.choice(valid_types),
            "amount": random.randint(10, 100)
        })

    return expenses