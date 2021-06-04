import datetime
"""
The point of this code is to return a 1 if the day is a work day
and a 0 if it isin't
return 1 = work day
return 0 = off day
"""

def workday_check(day, month, year):
    weekday = datetime.date(year, month, day).weekday()
    if (weekday==5 or weekday==6):
        return 0
    else:
        return 1