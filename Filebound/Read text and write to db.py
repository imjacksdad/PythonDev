import os
import csv
import pyodbc

location = 'C:/Python39/DEVFiles/PythonDev/Filebound/'
substring = 'filebound_data.csv'

#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEDSQL050;'
                      'Database=Filebound;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#Loop through directory
for file in os.listdir(location):
    #look for only CSV files
    if file.endswith(".csv"):
        if substring in file:
        
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
                            #sql_insert_query = "INSERT INTO Filebound (FileID,ProjectID,Status,DateChanged,Destruction,Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9,Field10,DateCreated,DateStarted,Changed) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                            #val=[row[0],row[1],row[2],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35]]

                            sql_insert_query = "INSERT INTO Files (ProjectID,Status) VALUES (?,?)"
                            val=[row[1],row[2]]


                            ##,row[3] removed.
                            cursor.execute(sql_insert_query, val)                

                            conn.commit()
                            print('Record inserted')
                            line_count += 1




By,LabelPrinted,UpdateFieldValueOld,CheckDone,BoxID,Field11,Field12,Field13,Field14,Field15,Field16,Field17,Field1,Field19,Field20,FilePtr,RemoteID,Locked
