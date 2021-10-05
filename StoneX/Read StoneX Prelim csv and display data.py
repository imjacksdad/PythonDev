import os
import csv
import pyodbc
from datetime import date
from time import strftime


#location = '\\\\tedfil01\\InformaticaDEV\\Process\\Position\\StoneX\\'
location = 'C:\\Python39\\DEVFiles\\PythonDev\\Support Files\\StoneX'
file = 'GAVPOS.csv'
#substring = 'Prelim.csv'

# Get today's date 
print("Today is " + strftime("%Y-%d-%m"))    #2021-05-20

#Open the file
with open(os.path.join(location, file)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        #BEGIN FOR
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #Write/Insert row info into database
                val = row[14]
                year = val[0:4]
                month = val[4:6]
                day = val[6:8]
                
                #print(val)
                #print("Year is: " + year)
                #print("Month is: " + month)
                #print("Day is: " + day)
                #print()

                f_date = date(int(val[0:4]), int(val[4:6]), int(val[6:8]))
                t_date = date.today()
                delta = t_date - f_date
                
                print(f_date)
                print(t_date)
                print(str(delta.days) + ' days')
                print()

                line_count += 1
