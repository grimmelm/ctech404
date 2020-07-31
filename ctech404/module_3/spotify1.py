import requests, sys
from spotifysecrets import *
from base64 import b64encode

AUTHENTICATION_URL = 'https://accounts.spotify.com/api/token'

# Authenticate with Spotify
headers = {'Authorization':
           b'Basic ' + b64encode(CLIENT_ID + b':' + CLIENT_SECRET)}
body = {'grant_type': 'client_credentials'}
r = requests.post(AUTHENTICATION_URL, headers=headers, data=body)

token = r.json()['access_token']
print('Request URL: ' + AUTHENTICATION_URL)
print('Request header: ' + headers)
print('Request body: ' + body)
print('Response body: ' + r.text)
print('Token: ' + token)
