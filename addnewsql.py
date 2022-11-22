
import sqlite3
import json


file = 'dbdb.db'
connection = sqlite3.connect(file)

cursor = connection.cursor()

f = open('db.json')

data = json.load(f)

aa = data["quotes"]



Tempscript = """

create table if not exists Quotes(
quotes TEXT);


"""

cursor.executescript(Tempscript)

for i in aa:
    print(i)
    q = f"select * from Quotes where quotes like '{i}'"
    r = cursor.execute(q)
    datadata = list(r)
    print(datadata)
    if len(datadata) == 0:
        q = f'insert into Quotes (quotes) values ("{i}")'
        cursor.execute(q)
    connection.commit()





query = "select quotes from Quotes"
cursor.execute(query)
result = cursor.fetchall()
connection.commit()
print(result)

