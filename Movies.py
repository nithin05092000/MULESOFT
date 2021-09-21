import sqlite3
from sqlite3.dbapi2 import Cursor
connection = sqlite3.connect("movies1.db")
Cursor = connection.cursor()

command1 = """
    CREATE TABLE [MOVIESTABLE](
[TITLE] NVARCHAR(100) NOT NULL,
[ACTOR] NVARCHAR(100) NOT NULL,
[ACTRESS] NVARCHAR(100) NOT NULL,
[DIRECTOR] NVARCHAR(100) NOT NULL,
[YEAR] INTEGER(10) NOT NULL);

"""
Cursor.execute(command1)
print("Table created")

# add values to the table
Cursor.execute(
    "INSERT INTO MOVIESTABLE VALUES('PUSHPA','ALLU ARJUN','RASHMIKA','SUKUMAR',2022)")
Cursor.execute(
    "INSERT INTO MOVIESTABLE VALUES('EEGA','NANI','SAMANTHA','RAJAMOULI',2012)")
Cursor.execute(
    "INSERT INTO MOVIESTABLE VALUES('HYPER','RAM','RASHI','SANTHOSH',2016)")
Cursor.execute(
    "INSERT INTO MOVIESTABLE VALUES('SYPDER','MAHESH','RAKUL','MURUDADOSS',2017)")
Cursor.execute(
    "INSERT INTO MOVIESTABLE VALUES('SAHOO','PRABHAS','SHRADDHA','SUJEETH',2019)")

# get query results

# QUERY 1
Cursor.execute("SELECT * FROM MOVIESTABLE")
results = Cursor.fetchall()
print(results)

# QUERY 2
Cursor.execute("SELECT TITLE FROM MOVIESTABLE WHERE ACTOR='ALLU ARJUN'")
results1 = Cursor.fetchone()
print(results1)


connection.commit()
connection.close()
