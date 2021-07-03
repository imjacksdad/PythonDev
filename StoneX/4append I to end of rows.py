import csv

path = 'C:\\Python39\\DEVFiles\\PythonDev\\Support Files\\StoneX\\'

with open(path + 'GAVPOS.csv', 'r+') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    #BEGIN FOR
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            row.append("PositionType")
            #print(row)
            csv_file.write(str(row))  #puts the [] around the row since it's a list converted to a string.  Will need to strip [] out before writing.
            line_count += 1
        elif {row[0]} == "PRECID":
            print('This is the header row')
            row.append("PositionType")
            print(row)
            line_count -= 1
        else:
            #print(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[65]},,')
            row.append("I")
            #print(f'\t{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[66]},,')
            print(row)

            line_count += 1
            
print(f'Processed {line_count} lines.')
