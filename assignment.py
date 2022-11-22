from flask import Flask, request
from flask_cors import CORS
import random
import json
from loadsql import loadsqlmain
import addnewsql


app = Flask(__name__)   # creates a flask server with name/handle of app
CORS(app)               # applies cross domain object requests to app

alldata1 = loadsqlmain()
alldata = alldata1["alllist"]
quotes1 = alldata1["quotes"]
jokes1 = alldata1["jokes"]
factoftheday1 = alldata1["fact-of-the-day"]

aa = random.choice(alldata)
print(aa)


@app.route("/")
def main():
    aa = random.choice(alldata)
    print(aa)
    if aa in jokes1:
        bb = "Jokes"
    if aa in quotes1:
        bb = "Quotes"
    if aa in factoftheday1:
        bb = "Fact of the day"
    return f"""
    <h1>{aa}</h1>
    {bb}
    """

@app.route("/post", methods=['POST'])
def post():
    returnn = None
    payload = request.form
    data = dict(payload)
    for i in alldata1:
        if data["post1"] in i:
            print(data["post1"])
            returnn = True
    if returnn == None:
        if data["type"] == "quotes":
            addnewsql.addnewQuote(data["post1"])
        elif data["type"] == "jokes":
            addnewsql.addnewJokes(data["post1"])
        elif data["type"] == "factoftheday":
            addnewsql.addnewFactoftheday(data["post1"])
    addnewsql.save()
    return "True"







app.run()