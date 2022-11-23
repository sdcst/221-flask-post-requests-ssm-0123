from flask import Flask, request
from flask_cors import CORS
import random
from loadsql import loadsqlmain
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
    returnn = None
    payload = request.form
    data = dict(payload)
    token = data["post1"]
    q = f"select * from Quotes where quotes like '{token}'"
    r = cursor.execute(q)
    datadata = list(r)
    if len(datadata) == 0:
        q = f'insert into Quotes (quotes) values ("{token}")'
        cursor.execute(q)
        
    return 







app.run()