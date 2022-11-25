from os import close
from flask import Flask, request
from flask_cors import CORS
import random
import sqlite3


app = Flask(__name__)   # creates a flask server with name/handle of app
CORS(app)               # applies cross domain object requests to app

file = 'dbdb.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()


alldata = []
query = "select quotes from Quotes"
cursor.execute(query)
result = cursor.fetchall()
quotes = result
for i in quotes:
    alldata.append(i[0])

connection.close()

aa = random.choice(alldata)
print(aa)


@app.route("/")
def main():
    aa = random.choice(alldata)
    print(aa)
    return f"""
    <h1>{aa}</h1>
    """

@app.route("/post", methods=['POST'])
def post():
    cursor = connection.cursor()
    payload = request.form
    data = dict(payload)
    token = data["post1"]
    for i in alldata:
        if token in i:
            return "It does already exist"

    q = f'insert into Quotes (quotes) values ("{token}")'
    cursor.execute(q)
    connection.commit()
    connection.close()
    return f"""
    {data["post1"]} is added
    """



@app.route("/requestlist", methods=['POST','GET'])
def listprint():
    connection = sqlite3.connect(file)
    cursor = connection.cursor()
    payload = request.form
    data = dict(payload)
    token = data["type"]
    requestdatalist =[]
    q = f"select * from {token}"
    r = cursor.execute(q)
    datadata = list(r)
    for i in datadata:
        requestdatalist.append(i[0])
    requestdatalist = sorted(requestdatalist)
    returnn = ""
    for i in requestdatalist:
        returnn = returnn +"\n" +i
    connection.close()
    return returnn





app.run()