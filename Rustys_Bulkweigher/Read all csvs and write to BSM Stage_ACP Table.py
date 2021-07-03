import os
import csv
import pyodbc

from datetime import date

location = 'C:\\Python39\\DEVFiles\\PythonDev\\Support Files\\BSM'

# Get today's date 
today = date.today()
#print(today)
#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEDSQL050;'
                      'Database=FreightExecution;'
                      'Trusted_Connection=yes;'
                      'Driver={ODBC Driver 17 for SQL Server};')
cursor = conn.cursor()

brg_keyword = 'BRG'
bri_keyword = 'BRI'
bro_keyword = 'BRO'
dem_keyword = 'DEM'
des_keyword = 'DES'
for_keyword = 'FOR'
fum_keyword = 'FUM'
ins_keyword = 'INS'
mis_keyword = 'MIS'


#Loop through directory
for file in os.listdir(location):
    #look for only CSV files
    #if file.endswith(".csv"):
        #if substring in file:
        if brg_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1

        elif bri_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1


        elif bro_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1


        elif dem_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1

        elif des_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1


        elif for_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1


        elif fum_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1


        elif ins_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1


        elif mis_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1


        elif des_keyword in file:
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
                                a = row[7]
                                if a:
                                    #Write/Insert row info into database
                                    sql_insert_query = "INSERT INTO Stage_ACP \
                                    ([Location],[ProfileId],[VoucherAmount],[VoyageReference],[ContractNumber], \
                                    [InvoiceNumber],[VoucherDescVoyRef],[VoucherDesc3Code],[VoucherDescVessel], \
                                    [CurrencyCode],[CommodityCode]) \
                                    VALUES \
                                    (?,?,?,?,?,?,?,?,?,?,?)"
                                    #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
                                    val=[row[0],row[1],row[2],row[3],row[4],row[5], \
                                         row[6],row[7],row[8],row[9],row[10]]

                                    #print(sql_insert_query, val)
                                    cursor.execute(sql_insert_query, val)                

                                    conn.commit()

                                    print('Record inserted')
                                    print()
                                    print()
                                    line_count += 1

        

