import os
import csv
import pyodbc
from datetime import date

#location = '\\\\tedfil01\\InformaticaDEV\\Process\\Position\\StoneX\\'
location = 'C:\\Python39\\DEVFiles\\PythonDev\\Support Files'
file = 'GAVPOS.csv'
#substring = 'Prelim.csv'

# Get today's date 
today = date.today()
print(today)    #2021-05-20

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
                val=row[14]
                
                print(val)

                line_count += 1
