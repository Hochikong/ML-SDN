import requests
import json
print('getname')
url = raw_input('Enter the address')
name = raw_input("Enter the name')
payload = {'name':name}
headers = {'content-type':'application/json'}
r = requests.post(url,data=json.dumps(payload),headers=headers)
print(r.content)
