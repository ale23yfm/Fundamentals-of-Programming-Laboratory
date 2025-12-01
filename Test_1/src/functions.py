#
# Functions section
#

def add_phone(phones, manufacturer, model, price):
    """
    The function adds a new phone to the list of dictionaries of phones
    :param phones: the list of dictionaries of phones
    :param manufacturer: the manufacturer of the phone, string
    :param model: the model of the phone, string
    :param price: the price of the phone, positive integer
    """

    if len(manufacturer) < 3:
        raise ValueError("Invalid manufacturer input. It must contain at least 3 characters.")
    if len(model) < 3:
        raise ValueError("Invalid model input. It must contain at least 3 characters.")

    phones.append({"manufacturer": manufacturer,
                   "model":model,
                   "price":price})

def find_by_manufacturer(phones, manufacturer, cnt):
    """
    The function searches all the phones from a given manufacturer.
    :param phones: the list of dictionaries of phones
    :param manufacturer: the manufacturer of the phone, string
    :param cnt: the contor to verify if there are any phones
    :return: the list of dictionaries that have a specified manufacturer and the contor to verify if anything was found
    """

    result = [] # a temporary list of dictionaries
    for p in phones:
        if p["manufacturer"] == manufacturer:
            result.append(p)
            cnt += 1

    return result, cnt

def increase_price(phones, manufacturer, model, amount, cnt):
    """
    The function increases the price of a phone my a given amount.
    :param phones: the list of dictionaries of phones
    :param manufacturer: the manufacturer of the phone, string
    :param model: the model of the phone, string
    :param amount: the amount which should be added to the phone's price, positive integer
    :param cnt: the contor to verify if there was any price updated
    :return: the list of dictionaries of phones with updated price and the contor for verifying if anything was updated
    """

    for p in phones:
        if p["manufacturer"] == manufacturer and p["model"] == model:
            p["price"] = p["price"] + amount
            cnt += 1

    return phones, cnt

def increase_by_percent(phones, percent):
    """
    The function increases all the prices with the given percent
    :param phones: the list of dictionaries of phones
    :param percent: the percent of the price to be added to the price, between -50 and 100
    :return: the list of dictionaries of phones with updated prices
    """

    for p in phones:
        add = int((percent * p["price"])/100)
        p["price"] = p["price"] + add

    return phones