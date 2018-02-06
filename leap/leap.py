def is_leap_year(year):
    try:
        number = int(year)
    except ValueError:
        raise Exception("Expecting a number here")
    else:
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

