import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("sybase+pyodbc://zec0009:Sunday07@INST01")


from sqlalchemy import text

with engine.connect() as connection:
    result = connection.execute(text("SELECT contractnumber FROM Position.AllPositionsFinal"))
    for row in result:
        print("contractnumber:", row['contractnumber'])
