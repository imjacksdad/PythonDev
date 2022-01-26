#import sqlanydb

# Create a connection object
#con = sqlanydb.connect( userid="zec0009", 
                       # password="Sunday07" )

# Close the connection
#con.close()

import pydobc

con = pydobc.connect(dsn="myDSN")
