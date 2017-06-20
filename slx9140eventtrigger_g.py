import json
import requests

payload = {'who': 'I_am_Gokuu', 'vote': 'goku'}
url = 'https://192.168.0.5/api/v1/webhooks/slx_with_gokuu'
print(url)
headers = {"Content-Type": "application/json", "St2-Api-Key": ""}

r = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

print(r.json)
