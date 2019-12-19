import json, time
import flask
import basicdb

DATABASE = 'tooter.json'


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
   
@app.route('/get-toots')
def get_toots():
    toots = basicdb.orderby(basicdb.sql_from('toots'), 'time')))[-5:]
    return json.dumps(latest_toots)

@app.route('/post-toot')
def post_toot():
    token = request.headers['Token']
    if token not in sessions:
        return 'Invalid token', 401
    toot = {'userid': sessions[token],
            'time': str(time.time()), 
            'text': request.form['text']}
    if len(toot['text'] > 100):
        return 'Toot too long', 403
    insert('toots', toot)
    basicdb.insert('toots', toot)
    return 'Toot posted'


# Setup
app = Flask(__name__)
basicdb.load_db(DATABASE)

logins = {}
for row in basicdb.sql_from('passwords'):
    logins[row['userid']] = row['password']

sessions = {}


app.run(host='0.0.0.0')