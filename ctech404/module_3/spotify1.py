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

from requests_toolbelt.utils import dump
data = dump.dump_all(r, request_prefix = '', response_prefix='')
print(data.decode('utf-8'))

print('\nToken: ' + token)
