import requests

url = 'http://127.0.0.1:5000/savefiletodrive'


r = requests.post(url, data={'flag': True})
print(r.json())