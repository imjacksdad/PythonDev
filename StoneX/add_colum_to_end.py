import csv

path = 'C:\Python39\DEVFiles\PythonDev\Support Files\\'
filename = 'GAVPOS.csv'
d = ','
f = open(path + filename,'r')

reader = csv.reader(f,delimiter=d)

# Read first line and count columns
ncol = len(next(reader))

#print out the number of columns
print("There are", ncol, "columns in this file.")

ncol = ncol + 1

print(ncol)

if reader startswith("PRECID") #then skip
    #else add "I" to the end of the line.
else 
##for x in range(1,int(ncol)):
##    print(x)
##
##f.seek(0)              # go back to beginning of file
##for row in reader:
##    print (str(x) + " - " + str(row))
##    
