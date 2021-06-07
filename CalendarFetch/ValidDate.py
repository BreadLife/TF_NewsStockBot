import datetime
import holidays
from DataCollection import _data
from DataCollection import _label

day = 1
month = 5
year = 2020
us_holidays = holidays.CountryHoliday(years=[2020], country='US', prov=None)

def number_of_days_in_month(month):
    if month == 1:      #Janvier
        return 31
    elif month == 2:    #Février
        return 28
    elif month == 3:    #Mars
        return 31
    elif month == 4:    #Avril
        return 30
    elif month == 5:    #Mai
        return 31
    elif month == 6:    #Juin
        return 30
    elif month == 7:    #Juilet
        return 31
    elif month == 8:    #Aout
        return 31
    elif month == 9:    #Septembre
        return 30
    elif month == 10:   #Octobre
        return 31
    elif month == 11:   #Novembre
        return 31
    elif month == 12:   #Décembre
        return 31

def is_it_a_holiday(year, month, date):
    day = str(year) + '-' + str(month) + '-' + str(date)
    answer = day in us_holidays
    if answer == True:
        return 1
    elif answer == False:
        return 0

def workday_check(year, month, day):
    weekday = datetime.date(year, month, day).weekday()
    if (weekday==5 or weekday==6):
        return 0
    else:
        return 1

def operable_day(year, month, day):
    if is_it_a_holiday(year, month, day) == 0 and workday_check(year, month, day) == 1:
        return 1
    else:
        return 0

"""
while(day <= number_of_days_in_month(month)):
    print(str(year) + '-' + str(month) + '-' + str(day) + "\n")
    print("Holiday: " + str(is_it_a_holiday(year, month, day)) + "\n")
    print("Workday: " + str(workday_check(year, month, day)) + "\n")
    day+=1
"""
