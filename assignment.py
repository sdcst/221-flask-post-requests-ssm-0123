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
    payload = request.form
    data = dict(payload)
    token = data["post1"]
    for i in alldata:
        if token in i:
            return "It does already exist"

    q = f'insert into Quotes (quotes) values ("{token}")'
    cursor.execute(q)
    connection.commit()
    return """
    Hello
    """


"""
@app.route("/requestlist", methods=['POST','GET'])
def listprint():
    
    payload = request.form
    data = dict(payload)
    token = data["hello"]
    allQuotes = []
    q = f"select * from Quotes"
    r = cursor.execute(q)
    datadata = list(r)
    for i in data:
        allQuotes.append(i[0])
    allQuotes = sorted(allQuotes)

    return 
"""




app.run()