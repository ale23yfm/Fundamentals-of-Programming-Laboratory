from functions import add_expense, remove_apartment, remove_apartments_range, remove_type, replace_amount

#A tests
def test_add_expense_valid():
    expenses = []
    history = []

    add_expense(expenses, history, 2, "gas", 30)

    # Check that the expense was added correctly
    assert len(expenses) == 1
    assert expenses[0]["apartment"] == 2
    assert expenses[0]["type"] == "gas"
    assert expenses[0]["amount"] == 30

    # Check that history was updated
    assert len(history) == 1

def test_add_expense_invalid():
    expenses = []
    history = []

    # Invalid apartment
    try:
        add_expense(expenses, history, -5, "gas", 100)
        assert False, "Expected ValueError for negative apartment"
    except ValueError:
        pass

    # Invalid type
    try:
        add_expense(expenses, history, 10, "internet", 50)
        assert False, "Expected ValueError for invalid type"
    except ValueError:
        pass

    # Invalid amount
    try:
        add_expense(expenses, history, 10, "gas", "a")
        assert False, "Expected ValueError for negative amount"
    except ValueError:
        pass

#B tests
def test_remove_apartment_valid():
    expenses = [
        {"apartment": 1, "type": "water", "amount": 50},
        {"apartment": 2, "type": "gas", "amount": 100},
        {"apartment": 1, "type": "heating", "amount": 75}
    ]
    history = [    ]

    remove_apartment(expenses, history, 1)

    # Check that all apartment 1 expenses were removed
    for e in expenses:
        assert e["apartment"] != 1

    # Check that history was updated
    assert len(history) == 1

    assert len(expenses) == 1
    assert expenses[0]["apartment"] == 2


def test_remove_apartment_invalid():
    expenses = [
        {"apartment": 1, "type": "water", "amount": 50},
        {"apartment": 2, "type": "gas", "amount": 100},
        {"apartment": 1, "type": "heating", "amount": 75}
    ]
    history = []

    try:
        remove_apartment(expenses, history, -5)
        assert False, "Expected ValueError for negative apartment"
    except ValueError:
        pass

    try:
        remove_apartment(expenses, history, "a")
        assert False, "Expected ValueError for non-integer apartment"
    except ValueError:
        pass

def test_remove_apartments_range_valid():
    expenses = [
        {"apartment": 1, "type": "water", "amount": 50},
        {"apartment": 2, "type": "gas", "amount": 100},
        {"apartment": 3, "type": "heating", "amount": 75},
        {"apartment": 4, "type": "electricity", "amount": 55},
        {"apartment": 5, "type": "other", "amount": 70}
    ]
    history = [ ]

    remove_apartments_range(expenses, history, 2, 3)
    # Check that all apartments 2 and 3 expenses were removed
    for e in expenses:
       assert e["apartment"] not in [2, 3]

    remaining_apt = [e["apartment"] for e in expenses]
    assert remaining_apt ==[1,4,5]

    # Check that history was updated
    assert len(history) == 1

def test_remove_apartments_range_invalid():
    expenses = [
        {"apartment": 1, "type": "water", "amount": 50},
        {"apartment": 2, "type": "gas", "amount": 100},
        {"apartment": 3, "type": "heating", "amount": 75},
        {"apartment": 4, "type": "electricity", "amount": 55},
        {"apartment": 5, "type": "other", "amount": 70}
    ]
    history = []

    try:
        remove_apartments_range(expenses, history, -5, 3)
        assert False, "Expected ValueError for negative apartment"
    except ValueError:
        pass

    try:
        remove_apartments_range(expenses, history, 4, "a")
        assert False, "Expected ValueError for non-integer apartment"
    except ValueError:
        pass

def test_remove_type_valid():
    expenses = [
        {"apartment": 1, "type": "gas", "amount": 50},
        {"apartment": 2, "type": "gas", "amount": 100},
        {"apartment": 1, "type": "heating", "amount": 75}
    ]
    history = [    ]

    remove_type(expenses, history, "gas")

    # Check that all apartment 1 expenses were removed
    for e in expenses:
        assert e["type"] != "gas"

    # Check that history was updated
    assert len(history) == 1

    assert len(expenses) == 1
    assert expenses[0]["type"] == "heating"


def test_remove_type_invalid():
    expenses = [
        {"apartment": 1, "type": "water", "amount": 50},
        {"apartment": 2, "type": "gas", "amount": 100},
        {"apartment": 1, "type": "heating", "amount": 75}
    ]
    history = []

    try:
        remove_type(expenses, history, 5)
        assert False, "Expected ValueError for integer type"
    except ValueError:
        pass

    try:
        remove_type(expenses, history, "a")
        assert False, "Expected ValueError for invalid type"
    except ValueError:
        pass

def test_replace_amount_valid():
    expenses = [
        {"apartment": 1, "type": "water", "amount": 50},
        {"apartment": 2, "type": "gas", "amount": 100},
        {"apartment": 1, "type": "heating", "amount": 75}
    ]
    history = []

    replace_amount(expenses, history, 1, "water", 100)

    # Check that the specific expense amount was updated
    for e in expenses:
        if e["apartment"] == 1 and e["type"] == "water":
            assert e["amount"] == 100

    # Check that other expenses are unchanged
    assert any(e["apartment"] == 2 and e["type"] == "gas" for e in expenses)
    assert any(e["apartment"] == 1 and e["type"] == "heating" for e in expenses)

    # Check that history was updated
    assert len(history) == 1

def test_replace_amount_invalid():
    expenses = [
        {"apartment": 1, "type": "water", "amount": 50},
        {"apartment": 2, "type": "gas", "amount": 100}
    ]
    history = []

    # Invalid apartment (negative)
    try:
        replace_amount(expenses, history, -1, "water", 100)
        assert False, "Expected ValueError for negative apartment"
    except ValueError:
        pass

    # Invalid apartment (non-integer)
    try:
        replace_amount(expenses, history, "a", "water", 100)
        assert False, "Expected ValueError for non-integer apartment"
    except ValueError:
        pass

    # Invalid type (not in valid_types)
    try:
        replace_amount(expenses, history, 1, "internet", 100)
        assert False, "Expected ValueError for invalid expense type"
    except ValueError:
        pass

    # Invalid amount (negative)
    try:
        replace_amount(expenses, history, 1, "water", -50)
        assert False, "Expected ValueError for negative amount"
    except ValueError:
        pass

    # Invalid amount (non-integer)
    try:
        replace_amount(expenses, history, 1, "water", "abc")
        assert False, "Expected ValueError for non-integer amount"
    except ValueError:
        pass

def run_all_tests():
    test_add_expense_valid()
    test_add_expense_invalid()
    test_remove_apartment_valid()
    test_remove_apartment_invalid()
    test_remove_apartments_range_valid()
    test_remove_apartments_range_invalid()
    test_remove_type_valid()
    test_remove_type_invalid()
    test_replace_amount_valid()
    test_replace_amount_invalid()
    print("All tests passed!")

