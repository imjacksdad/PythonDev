# Python SQL Select Statement Example
import pyodbc
import os
import csv

#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=tepsql050;'
                      'Database=CentralHedge;'
                      'Trusted_Connection=yes;')
#try:
cursor = conn.cursor()

cursor.execute('SELECT top 100 * FROM [CentralHedge].[dbo].[vw_ExchangeExtract] WHERE sourceId = \'89\'')
#Create new csv file to write to
FILE_WRITE = open('C:/Python39/DEVFiles/PythonDev/Output/test.csv','a')
records = cursor.fetchall()
field_names = [val[0] for val in cursor.description]

#wait = input("Press Enter to continue.")
print("\nPrinting each record")
for column in records:
    print("===========NEW RECORD===========")
    print("ExchangeId =", column[0], )
    print("ExchangeEventTypeId =", column[1], )
    print("ExchangeTypeId =", column[2], )
    print("SourceId =", column[3], )
    print("Action =", column[4], )
    print("Destruction =", column[5], )
    print("Unique_Trade_ID =", column[6], )
    print("Group_Trade_Id =", column[7], )
    print("GMI_ACCOUNT =", column[8], )
    print("Buy_SELL =", column[9], )
    print("QTY =", column[10], )
    print("BBG_SYMBOL =", column[11], )
    print("TRADE_PRICE =", column[12], )
    print("Exchange =", column[13], )
    print("Product_Code =", column[14], )
    print("Contract_MTHYR =", column[15], )
    print("Customer =", column[16], )
    print("FCM =", column[17], )
    #print("Customer_Account =", column[18] )

    with open('mytable1.txt', 'a') as f:    #a = append, w=write/overwrite
        #for row in records:
           f.write(str(column[0]) + '\n')

conn.close()

print("SQL connection is closed")
