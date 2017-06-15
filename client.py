import sys
import json
import requests

conv = {'Name': 'Temperature', 'Data': '25'}
s = json.dumps(conv)
# res = requests.post("http://FlaskWebAppTest.mybluemix.net/receiveData/", json=s).json()
r = requests.post('http://localhost:5000/', json=s)
print r.status_code