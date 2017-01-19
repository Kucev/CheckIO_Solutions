import datetime
def checkio(year):
    s = 0
    for i in range(1, 13):
        if datetime.date(year, i, 13).isoweekday() == 5:
            s += 1
    return s
