def add_festival(festivals, name, month, tc, la):
    """
    The function adds a new festival to the existing list of dictionaries.
    :param festivals: the list of dictionaries for the festivals
    :param name: the name of the festival, string
    :param month: the month when the festival happens, integer between 1 and 12
    :param tc: the ticket cost, integer
    :param la: list of artists
    """
    festivals.append({
        "name": name,
         "month": month,
         "ticket cost": tc,
         "a list of artists": la
         })

def asc_sort_by_month(festivals):
    festivals.sort(key=lambda x: x["month"])

def display_season(festivals, season):
    result =[]
    for f in festivals:
        if season == "winter":
            if f["month"] == 12:
                result.append(f)
            elif f["month"] == 1:
                result.append(f)
            elif f["month"] == 2:
                result.append(f)
        elif season == "spring":
            if f["month"] == 3:
                result.append(f)
            elif f["month"] == 4:
                result.append(f)
            elif f["month"] == 5:
                result.append(f)
        elif season == "summer":
            if f["month"] == 6:
                result.append(f)
            elif f["month"] == 7:
                result.append(f)
            elif f["month"] == 8:
                result.append(f)
        else:
            if f["month"] == 9:
                result.append(f)
            elif f["month"] == 10:
                result.append(f)
            elif f["month"] == 11:
                result.append(f)
    asc_sort_by_month(result)
    return result

def display_by_artist(festivals, la, cnt):
    result =[]
    for f in festivals:
        if la in f["a list of artists"]:
            result.append(f)
            cnt += 1
    asc_sort_by_month(result)
    return result, cnt