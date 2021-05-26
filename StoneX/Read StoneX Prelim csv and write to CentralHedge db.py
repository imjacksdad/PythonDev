import os
import csv
import pyodbc
from datetime import date

#location = '\\\\tedfil01\\InformaticaDEV\\Process\\Position\\StoneX\\'
location = 'C:\\Python39\\DEVFiles\\PythonDev\\Support Files'
file = 'Prelim.csv'
#substring = 'Prelim.csv'

# Get today's date 
today = date.today()
print(today)    #2021-05-20

#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEDSQL050;'
                      'Database=CentralHedge;'
                      'Trusted_Connection=yes;'
                      'Driver={ODBC Driver 17 for SQL Server};')
cursor = conn.cursor()

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
                sql_insert_query = "INSERT INTO StageStoneXPrelimFile \
                ([SCHEDULE_ID],[USERNAME],[Last_Business_Date],[FRECID],[FCHIT],[FFIRM],[FOFFIC],[FACCT],[FSUBAC],[FATYPE],\
                [FCUSIP],[SUNDCN],[FCTYM],[FSTYPE],[FSUBTY],[FSTRIK],[FEXPDT],[FEXPDT_DT],[FTDATE],[FTDATE_DT],\
                [FBS],[FSPRED],[FCLASS],[FSUBCL],[FRR],[FQTY],[FSDSC1],[FMKVAL],[FMULTF],[FSDATE_DT],\
                [FSDATE],[FLTDAT_DT],[FLTDAT],[FEXCH],[FFC],[FSYMBL],[FPTYPE],[FTPRIC],[FCLOSE],[FCURSY],\
                [FCALC],[FCMNT1],[FOC],[FEXBKR],[FOPBKR],[FGIVIO],[FGIVF#],[FCOMM],[FFEE1],[FFEE2],\
                [FFEE3],[FFEE4],[FGICHG],[FBKCHG],[FOTHER],[FGROSS],[FNET],[FTRACE],[Prodct],[ENV],\
                [FRTHT],[FUCUSP],[FUNDCP],[FATCOM],[FATFE1],[FATFE2],[FATFE3],[FATFE4],[FATFE5],[FATFE6],\
                [FATFE7],[FATFE8],[FATFE9],[FATGIV],[FATBKG],[FATOTH],[FATBKO],[FATFLR],[FATORD],[FATWIR],\
                [FATALO],[FFUFE1],[FFUFE2],[FFUFE3],[FFUFE4],[FFUFE5],[FFUFE6],[FFUFE7],[FFUFE8],[FFUFE9],\
                [FFUGIV],[FFUBKG],[FFUOTH],[FFUBKO],[FFUFLR],[FFUORD],[FFUWIR],[FFUALO],[FUSER],[FBQTY],\
                [FSQTY],[FPRTPR],[FRECNO],[FBATCH],[FCARD],[FDELET],[FSRCAC],[FTYPE],[FORDTY],[FTTYPE],\
                [FTBKT],[FCMNT2],[FCMNT3],[FIEXNG],[FIEFRM],[FDEAL],[FDEST],[FSDSC2],[FCURAT],[FSNAME],\
                [FREFNO],[FTRDEX],[FLEVEL],[FORDER],[FORDOR]) \
                VALUES \
                (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?\
                ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?\
                ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?\
                ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?\
                ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                val=[row[0],row[1],row[2],row[3],row[4],\
                     row[5],row[6],row[7],row[8],row[9],\
                     row[10],row[11],row[12],row[13],row[14],\
                     row[15],row[16],row[17],row[18],row[19],\
                     row[20],row[21],row[22],row[23],row[24],\
                     row[25],row[26],row[27],row[28],row[29],\
                     row[30],row[31],row[32],row[33],row[34],\
                     row[35],row[36],row[37],row[38],row[39],\
                     row[40],row[41],row[42],row[43],row[44],\
                     row[45],row[46],row[47],row[48],row[49],\
                     row[50],row[51],row[52],row[53],row[54],\
                     row[55],row[56],row[57],row[58],row[59],\
                     row[60],row[61],row[62],row[63],row[64],\
                     row[65],row[66],row[67],row[68],row[69],\
                     row[70],row[71],row[72],row[73],row[74],\
                     row[75],row[76],row[77],row[78],row[79],\
                     row[80],row[81],row[82],row[83],row[84],\
                     row[85],row[86],row[87],row[88],row[89],\
                     row[90],row[91],row[92],row[93],row[94],\
                     row[95],row[96],row[97],row[98],row[99],\
                     row[100],row[101],row[102],row[103],row[104],\
                     row[105],row[106],row[107],row[108],row[109],\
                     row[110],row[111],row[112],row[113],row[114],\
                     row[115],row[116],row[117],row[118],row[119],\
                     row[120],\
                     row[121],\
                     row[122],\
                     row[123],\
                     row[124]]

                print(sql_insert_query, val)
                cursor.execute(sql_insert_query, val)                

                conn.commit()
                print('Record inserted')
                line_count += 1
