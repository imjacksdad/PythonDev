# Python SQL Select Statement Example
import pyodbc

#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=tepsql050;'
                      'Database=Filebound;'
                      'Trusted_Connection=yes;')
#try:
cursor = conn.cursor()

cursor.execute('SELECT top 100 * FROM [FileBound].[dbo].[Files]')

#sql_select_Query = "SELECT * FROM [AgrisExtension].[Agris].[B01_TRANS]"
##for row in cursor:
##    print('row = %r' % (row,))
##    print()
#cursor.execute(sql_select_Query)

records = cursor.fetchall()
print("Total number of rows is: ", cursor.rowcount)

print("\nPrinting each record")
for column in records:
    print("===========NEW RECORD===========")
    print("FileID = ", column[0], )
    print("ProjectID = ", column[1], )
    print("Status = ", column[2], )
    print("Notes = ", column[3], )
    print("DateChanged = ", column[4], )
    print("Destruction = ", column[5], )
    print("Field1 = ", column[6], )
    print("Field2 = ", column[7], )
    print("Field3 = ", column[8], )
    print("Field4 = ", column[9], )
    print("Field5 = ", column[10], )
    print("Field6 = ", column[11], )
    print("Field7 = ", column[12], )
    print("Field8 = ", column[13], )
    print("Field9 = ", column[14], )
    print("Field10 = ", column[15], )
    print("DateCreated = ", column[16], )
    print("DateStarted = ", column[17], )
    print("ChangedBy = ", column[18], )
    print("LabelPrinted = ", column[19], )
    print("UpdateFieldValueOld = ", column[20], )
    print("CheckDone = ", column[21], )
    print("BoxID = ", column[22], )
    print("Field11 = ", column[23], )
    print("Field12 = ", column[24], )
    print("Field13 = ", column[25], )
    print("Field14 = ", column[26], )
    print("Field15 = ", column[27], )
    print("Field16 = ", column[28], )
    print("Field17 = ", column[29], )
    print("Field18 = ", column[3], )
    print("Field19 = ", column[31], )
    print("Field20 = ", column[32], )
    print("FilePtr = ", column[33], )
    print("RemoteID = ", column[34], )
    print("Locked = ", column[35], "\n")

##    sql_delete_query = """Delete from PackingList where BookingNumber = ?""" 
##    val = row[0]
##    print(sql_delete_query, val)
##    cursor.execute(sql_delete_query, val)
##    conn.commit()
##    print('Records deleted')
##    
##    sql_insert_query = "INSERT INTO PackingList ([FileID],[ProjectID],[Status],[Notes],[DateChanged],[Destruction],[Field1],[Field2],[Field3],[Field4],[Field5],[Field6],[Field7],[Field8],[Field9],[Field10],[DateCreated],[DateStarted],[ChangedBy],[LabelPrinted],[UpdateFieldValueOld],[CheckDone],[BoxID],[Field11],[Field12],[Field13],[Field14],[Field15],[Field16],[Field17],[Field18],[Field19],[Field20],[FilePtr],[RemoteID],[Locked]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
##    val=[column[0],column[2],column[3],column[4],column[5],column[7],column[8],column[9],column[10],column[11],column[12],column[17],column[18], column[19], column[20], column[21], column[22], column[23], column[24], column[25], column[26], column[27], column[28], column[29], column[30], column[31], column[32], column[33], column[34], column[35]]
##    print(sql_insert_query, val)        
##    cursor.execute(sql_insert_query, val)
##    conn.commit()
##    print('Record inserted')
         
##except Error as e:
##    print("Error reading data from SQL table", e)
##finally:
##    if (conn.is_connected()):

cursor.close()
conn.close()

print("SQL connection is closed")
