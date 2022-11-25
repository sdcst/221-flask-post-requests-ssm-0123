
import sqlite3

file = 'dbdb.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()


query = "select * from Quotes"
cursor.execute(query)
result = cursor.fetchall()
quotes = result

print(quotes)





"""
def loadsqlmain():

    file = 'dbdb.db'
    connection = sqlite3.connect(file)

    cursor = connection.cursor()


    query = "select quotes from ListofOutput"
    cursor.execute(query)
    result = cursor.fetchall()
    quotes = result


    query = "select jokes from ListofOutput"
    cursor.execute(query)
    result = cursor.fetchall()
    jokes = result


    query = "select factoftheday from ListofOutput"
    cursor.execute(query)
    result = cursor.fetchall()
    factoftheday = result




    quotes1 = []
    jokes1 = []
    factoftheday1 = []


    for a in quotes:
        if a[0] != None:
            quotes1.append(a[0])

    for a in jokes:
        if a[0] != None:
            jokes1.append(a[0])

    for a in factoftheday:
        if a[0] != None:
            factoftheday1.append(a[0])

    alllist = quotes1 + jokes1 + factoftheday1
    output = {
        "alllist" : alllist,
        "quotes" : quotes1,
        "jokes" : jokes1,
        "fact-of-the-day": factoftheday1
    }
    return output
"""