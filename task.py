
# importing sqlite3 module
import sqlite3

# defining connection and cursor
# training.db is the database created before
connection = sqlite3.connect('training.db')

cursor = connection.cursor()

# creating table movies with required required attributes[columns]
cmd1 = """CREATE TABLE  IF NOT EXISTS
MOVIES(NAME TEXT, ACTOR TEXT, ACTRESS TEXT, DIRECTOR TEXT,YEAR_OF_RELEASE INTEGER)"""

cursor.execute(cmd1)

# adding/inserting values into table movies
cursor.execute(
    "INSERT INTO MOVIES VALUES ('Hulk','Mark Ruffalo','','JON FAVREAU',2008)")
cursor.execute(
    "INSERT INTO MOVIES VALUES ('Ugram','Sri Muruli','Haripriya','Prashanth Neel',2014)")
cursor.execute(
    "INSERT INTO MOVIES VALUES ('Mungaru Male','Ganesh','Pooja Gandhi','Yograj Bhatt',2006)")
cursor.execute(
    "INSERT INTO MOVIES VALUES ('Simbha','Ranveer Singh','Sara Ali Khan','Rohith Shetty',2019)")
cursor.execute(
    "INSERT INTO MOVIES VALUES ('KGF','Yash','Srinidhi','Prashanth Neel',2016)")
cursor.execute(
    "INSERT INTO MOVIES VALUES ('DON','Sharukh','Priyanka','Farahan',2006)")


# querying data from the table
cursor.execute("SELECT * FROM MOVIES")
cursor.execute("SELECT NAME FROM MOVIES WHERE ACTOR='Ganesh'")
# the last query's output is displayed


# displaying the output
res = cursor.fetchall()
print(res)
