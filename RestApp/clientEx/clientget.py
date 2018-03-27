import json
import requests

headers = {'content-type': 'application/json'}
url = 'http://127.0.0.1:5000/data'
auth=('jits','python')
res = requests.get(url, auth = auth).json()
print(res)

