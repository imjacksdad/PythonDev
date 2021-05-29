from datetime import date
import calc_dates

today = date.today()

#Today
d0 = date.today()  #2021-05-18
print("d0 =", d0)

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")  #18/05/2021
print("d1 =", d1)

# Textual month, day and year	  #May 18, 2021
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m,%d,%y")  #05/18/21 or 05,26,2021
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")  #May-18-2021
#or feed in your own date
#d4 = 'May-19-2021'  
print("d4 =", d4)

# Year, month, day  --Used for a lot of STX, WFC, FMT, GMI 	
d5 = today.strftime("%Y%m%d")
print("d5 =", d5)


#pass the value of d4 to the calc_date funtion
calc_dates.calc_dates(d4)
#this will call the file.function


