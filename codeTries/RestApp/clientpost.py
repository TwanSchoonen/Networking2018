import json
import requests

headers = {'content-type': 'application/json'}
url = 'http://127.0.0.1:5000/data'
data = {"username":"miguel","password":"python"}

res = requests.post(url, data=json.dumps(data), headers=headers)
print(res)


