import requests
import base64
import json

url = 'http://127.0.0.1:5000/taketext'


r = requests.post(url, data={'text': "alright nigga save me"})
print(r.json())