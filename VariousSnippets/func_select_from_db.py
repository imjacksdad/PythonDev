import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEPDAGAGR01;'
                      'Database=AgrisExtension;'
                      'Trusted_Connection=yes;')


def getCommodity(commcode):
    #print(commcode)
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEPDAGAGR01;'
                      'Database=AgrisExtension;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    sql = 'SELECT top(1) [C05_COMM_CD_S], [C05_CMM_DESC_S] \
                FROM [Agris].[C05_COMMODITY_CODE] \
                WHERE [C05_COMM_CD_S] = \'' + commcode + '\''
    
    #print(sql)
    cursor.execute(sql)
    try:
        for row in cursor:
            print('The description for ' + str(row[0]) + ' is ' + str(row[1]))
    except:
        print("No matching results")
            
## END OF FUNCTION  ##


cur = conn.cursor()
sql = 'SELECT TOP(100) C05_COMM_CD_S\
                FROM [Agris].[C05_COMMODITY_CODE_PE]'
cur.execute(sql)
               
for cmdty in cur:
    cmdty = str(cmdty[0])
    #print(cmdty)
    getCommodity(str(cmdty))
