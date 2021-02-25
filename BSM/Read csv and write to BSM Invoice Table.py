import os
import csv
import pyodbc

from datetime import date

#location = '\\\\tedfil01\\InformaticaDEV\\Process\\StoneX\\'
location = 'C:\\Python39\\DEVFiles\\PythonDev\\BSM'
#substring = '20210225070848_invticket_1688.csv'


# Get today's date 
today = date.today()
#print(today)
#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEDSQL050;'
                      'Database=MDMStage;'
                      'Trusted_Connection=yes;'
                      'Driver={ODBC Driver 17 for SQL Server};')
cursor = conn.cursor()

keyword = 'invticket'

#Loop through directory
for file in os.listdir(location):
    #look for only CSV files
    #if file.endswith(".csv"):
        #if substring in file:
        if keyword in file:
            #Open the file
            with open(os.path.join(location, file)) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    
                    #BEGIN FOR
                    print('Inserting ' + file)
                    print()
                    print()
                    for row in csv_reader:
                        if line_count == 0:
                            #print(f'Column names are {", ".join(row)}')
                            line_count += 1
                        else:

                            #Write/Insert row info into database
                            sql_insert_query = "INSERT INTO stg_InvTicket \
                            ([Status],[BookingNumber],[Container],[Seal],[NetWeight],[VGM] \
                            ,[BSMNVOCCProfileID],[NVOCCName],[BSMTransloaderProfileID],[Transloader Name] \
                            ,[SupplierSourceCustomerID],[BsmSupplierProfileId],[BuyerSourceCustomerId] \
                            ,[BsmBuyerProfileId],[InternalSalesContract],[SaleContract],[BsmOrderId] \
                            ,[InvNumber],[OBD],[DestinationPortCode],[DestinationPortName] \
                            ,[Commodity],[Location],[Source],[SubSource],[FileDate]) \
                            VALUES \
                            (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                            #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                            val=[row[0],row[1],row[2],row[3],row[4],\
                                 row[5],row[6],row[7],row[8],row[9],\
                                 row[10],row[11],row[12],row[13],row[14],\
                                 row[15],row[16],row[17],row[18],row[19],\
                                 row[20],row[21],row[22],row[23],row[24],today]

                            print(sql_insert_query, val)
                            cursor.execute(sql_insert_query, val)                

                            conn.commit()

                            print('Record inserted')
                            print()
                            print()
                            line_count += 1
