from dateutil.relativedelta import *  #https://dateutil.readthedocs.io/en/stable/
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

#now = parse("Sat Oct 11 17:13:46 UTC 2003")

def calc_dates(d):
    #now = parse("Sat Oct 11 17:13:46 UTC 2003")
    #now = datetime.now()
    
    now = parse(d)   #https://dateutil.readthedocs.io/en/stable/parser.html
    today = now.date()
    year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
    rdelta = relativedelta(easter(year), today)
    yesterday = datetime.now() - timedelta(1)
    
    print("Today is: %s" % today)
    #Today is: 2003-10-11

    print("Year with next Aug 13th on a Friday is: %s" % year)
    #Year with next Aug 13th on a Friday is: 2004

    print("How far is the Easter of that year: %s" % rdelta)
    #How far is the Easter of that year: relativedelta(months=+6)

    print("And the Easter of that year is: %s" % (today+rdelta))
    #And the Easter of that year is: 2004-04-11

    print("And yesterday's date was: %s" % yesterday)

if __name__ == '__main__':
#   # get_date.py executed as script
#   # do something
    #d = "Sat Oct 11 17:13:46 UTC 2003"
    calc_dates(d)

