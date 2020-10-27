import requests
import json
url = 'https://drilling2020.herokuapp.com/'
data = {"Pclass":3, "Age":2, "SibSp":1, "Fare":50}
response = requests.post(url, json.dumps(data))
print(response.json())

curl -s -XPOST 'https://drilling2020.herokuapp.com/' -d '{"Pclass":3,"Age":2,"SibSp":1,"Fare":50}' -H 'accept-content: application/json'
