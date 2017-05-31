import json
import requests

payload = {'who': 'I_am_a_Frieza'}
url = 'https://172.24.182.70/api/v1/webhooks/slx_with_freeza'
print(url)
headers = {"Content-Type": "application/json", "St2-Api-Key": api_key}

r = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

print(r.json)
