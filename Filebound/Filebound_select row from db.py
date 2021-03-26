# Python SQL Select Statement Example
import pyodbc
import datetime



#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=tepsql050;'
                      'Database=Filebound;'
                      'Trusted_Connection=yes;')

#Create new csv file to write to
FILE_WRITE = open('C:/Python39/DEVFiles/PythonDev/Filebound/filebound_data.csv','a')
#try:
cursor = conn.cursor()

cursor.execute('SELECT top 100 * FROM [FileBound].[dbo].[Files]')


records = cursor.fetchall()
#print("Total number of columns is: ", cursor.rowcount)
print("Writing File, Please wait...")
##print("\nPrinting each record")
for column in records:
##    print("===========NEW RECORD===========")
##    print("FileID = ", column[0], )
##    print("ProjectID = ", column[1], )
##    print("Status = ", column[2], )
##    print("Notes = ", column[3], )
##    print("DateChanged = ", column[4], )
##    print("Destruction = ", column[5], )
##    print("Field1 = ", column[6], )
##    print("Field2 = ", column[7], )
##    print("Field3 = ", column[8], )
##    print("Field4 = ", column[9], )
##    print("Field5 = ", column[10], )
##    print("Field6 = ", column[11], )
##    print("Field7 = ", column[12], )
##    print("Field8 = ", column[13], )
##    print("Field9 = ", column[14], )
##    print("Field10 = ", column[15], )
##    print("DateCreated = ", column[16], )
##    print("DateStarted = ", column[17], )
##    print("ChangedBy = ", column[18], )
##    print("LabelPrinted = ", column[19], )
##    print("UpdateFieldValueOld = ", column[20], )
##    print("CheckDone = ", column[21], )
##    print("BoxID = ", column[22], )
##    print("Field11 = ", column[23], )
##    print("Field12 = ", column[24], )
##    print("Field13 = ", column[25], )
##    print("Field14 = ", column[26], )
##    print("Field15 = ", column[27], )
##    print("Field16 = ", column[28], )
##    print("Field17 = ", column[29], )
##    print("Field18 = ", column[3], )
##    print("Field19 = ", column[31], )
##    print("Field20 = ", column[32], )
##    print("FilePtr = ", column[33], )
##    print("RemoteID = ", column[34], )
##    print("Locked = ", column[35], "\n")

    #print(f'\t{column[0]},{column[1]},{column[2]},{column[3]},{column[4]},{column[5]},{column[6]},{column[7]},{column[8]},{column[9]},{column[10]},{column[11]},{column[12]},{column[13]},{column[14]},{column[15]},{column[16]},{column[17]},{column[18]},{column[19]},{column[20]},{column[21]},{column[22]},{column[23]},{column[24]},{column[25]},{column[26]},{column[27]},{column[28]},{column[29]},{column[30]},{column[31]},{column[32]},{column[33]},{column[34]},{column[35]}')
    FILE_WRITE.write(f'\t{column[0]},{column[1]},{column[2]},{column[4]},{column[5]},{column[6]},{column[7]},{column[8]},{column[9]},{column[10]},{column[11]},{column[12]},{column[13]},{column[14]},{column[15]},{column[16]},{column[17]},{column[18]},{column[19]},{column[20]},{column[21]},{column[22]},{column[23]},{column[24]},{column[25]},{column[26]},{column[27]},{column[28]},{column[29]},{column[30]},{column[31]},{column[32]},{column[33]},{column[34]},{column[35]}\n')
    ##Removed {column[3]} Note column because it was causing errors
    
FILE_WRITE.close()                            
cursor.close()
conn.close()

print("File dump complete.")
print("SQL connection is closed")
