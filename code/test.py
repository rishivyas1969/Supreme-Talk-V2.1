import requests
import base64
import json

url = 'http://127.0.0.1:5000/audiototext'

audio = open('recording1.wav', 'rb')

r = requests.post(url, files={'file': audio})
print(r.json())