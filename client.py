import sys
import json
import requests

conv = {'Name': 'Temperature', 'Data': '25'}
s = json.dumps(conv)
res = requests.post("http://127.0.0.1:5000/receiveData/", json=s).json()
print type(res)