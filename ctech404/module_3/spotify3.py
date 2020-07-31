import requests, sys
from spotifysecrets import *
from base64 import b64encode
import requestsview

AUTHENTICATION_URL = 'https://accounts.spotify.com/api/token'

# Authenticate with Spotify
headers = {'Authorization':
           b'Basic ' + b64encode(CLIENT_ID + b':' + CLIENT_SECRET)}
body = {'grant_type': 'client_credentials'}
r = requests.post(AUTHENTICATION_URL, headers=headers, data=body)

token = r.json()['access_token']
tokenHeaders = {'Authorization' : 'Bearer ' + token}

SEARCH_URL = 'https://api.spotify.com/v1/search'

# Find top artist matching the user's search
artistName = ' '.join(sys.argv[1:])
query = {'q': artistName, 'type': 'artist'}
r = requests.get(SEARCH_URL, headers=tokenHeaders, params=query)

requestsview.view(r)
