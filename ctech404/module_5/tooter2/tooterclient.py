import requests, sys

BASE_URL= 'http://localhost'
PORT = ":5000"

GET_ENDPOINT = BASE_URL + PORT + '/get-toots'
POST_ENDPOINT = BASE_URL + PORT + '/post-toot'


def login():
    u = input('Enter username: ')
    p = input('Enter password: ')
    r = requests.post(LOGIN_ENDPOINT, headers={'Username': u, 'Password': p})
    if r.ok:
        print(u + ' logged in')
        return r.json()['token']
    else:
        print(r.text)
        sys.exit()

 
def top_toots():
    r = requests.get(GET_ENDPOINT)
    if r.ok:
        print('-----TOOTS-----')
        for toot in reversed(r.json()):
            print(toot['userid'] + ' -> ' + toot['text'])
        print('---------------')
    else:
        print('Error: ' + r.text)

 
def post_toot(tokeen):
    t = input('Enter your toot: ')
    r = requests.post(POST_ENDPOINT, data={'text': t}, headers={'Token':token})
    if r.ok:
        print('Toot posted')
    else:
        print('Error: ' + r.text)




print('Welcome to Tooter!')
t = login()
while True:
    print('(0) quit')
    print('(1) read toots')
    print('(2) post toot')
    i = input('Enter command : ')
    if i == '0':
        break
    elif i == '1':
        get_toots()
    elif i == '2':
        post_toot(t)        
    else:
        print('Illegal command. Please try again.')




            