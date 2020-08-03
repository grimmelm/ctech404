import json, time
import flask
import basicdb

DATABASE = 'chirper.json'

# Setup
app = flask.Flask(__name__)
basicdb.load_db(DATABASE)

logins = {}
for row in basicdb.db_from('passwords'):
    logins[row['userid']] = row['password']

sessions = {}

@app.route('/login', methods=['POST'])
def login():
    username = request.header['Username']
    password = request.header['Password']
    if username not in logins:
         return 'No such user', 401
    if password != logins[username]:
         return 'Invalid password', 401
    token = secrets.token_hex()
    sessions[token] = username
    return token
   
@app.route('/get-chirps')
def get_chirps():
    chirps = basicdb.orderby(basicdb.db_from('chirps'), 'time')[-5:]
    return json.dumps(latest_chirps)

@app.route('/post-chirp')
def post_chirp():
    token = request.headers['Token']
    if token not in sessions:
        return 'Invalid token', 401
    chirp = {'userid': sessions[token],
            'time': str(time.time()), 
            'text': request.form['text']}
    if len(chirp['text']) > 100:
        return 'chirp too long', 403
    insert('chirps', chirp)
    basicdb.insert('chirps', chirp)
    return 'chirp posted'



app.run(host='0.0.0.0')
