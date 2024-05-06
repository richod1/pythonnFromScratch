import app
import datetime
import json

getDate=datetime.datetime.now()

app.greeting("Degraft")

print("today date is ", getDate.strftime("%A"))

myData='{ "name":"John", "age":30, "city":"New York"}'

dataToDict=json.loads(myData)

print(dataToDict)

# convering dict to json
X={
    "name":"Degraft",
    "age":22,
    "city":"Takoradi"
}

data_convert=json.dumps(X)
print(data_convert)