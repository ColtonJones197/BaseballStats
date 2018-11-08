import pypyodbc as pyodbc
import pandas as pd

db_host = 'DESKTOP-9UPPQHB'
db_name = 'RPlayGround'

connStr = ('Driver={SQL Server Native Client 11.0}; Server= '
           + db_host + ';Database = ' + db_name +
           ';Trusted_Connection=Yes;'
           + 'UID = jojo; PWD = Blizzard;')

db = pyodbc.connect(connStr)

SQLtxt = ('SELECT * FROM RPlayGround.dbo.rental_data;')

cursor = db.cursor()

cursor.execute(SQLtxt)

print(cursor.fetchone())

db.close()

print('Success!')

# TODO: Send API request, create class structure diagram
