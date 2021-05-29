from datetime import date
import calc_dates



def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    today = date.today()
    thisyear = today.year  #05/18/21 or 05,26,2021
    thismonth = today.month
    thisday = today.day
    
    print(thisyear)
    print(thismonth)
    print(thisday)

    d1 = thisyear,thismonth,thisday
    print(d1)
    d2 = date(2013,9,13)
    print(d2)
    result1 = diff_dates(d2, d1)
    print('{} days between {} and {}'.format(result1, d1, d2))

main()


from datetime import datetime
from datetime import date
import calc_dates

date_format = "%m/%d/%Y"
today = date.today()
print(today)
a = datetime.strptime(today, date_format)
b = datetime.strptime('9/26/2008', date_format)
delta = b - a
print(delta.days) # that's it
