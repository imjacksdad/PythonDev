from datetime import date

def get_days(yr, mo, day):
    f_date = date(yr, mo, day)
    l_date = date.today()
    #print(l_date)

    delta = l_date - f_date
    print(delta.days)

#get_days(2016, 7, 2)

    
