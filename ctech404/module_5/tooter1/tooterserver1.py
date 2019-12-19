import json, time
import flask
import basicdb

DATABASE = 'tooter.json'

# Setup
app = Flask(__name__)
basicdb.open_db(DATABASE)
   
@app.route('/get-toots')
def get_toots():
    toots = basicdb.orderby(basicdb.sql_from('toots'), 'time')))[-5:]
    return json.dumps(latest_toots)

@app.route('/post-toot', methods=['POST'])
def post_toot():
    toot = {'userid': flask.request.form['user'],
            'time': str(time.time()), 
            'text': flask.request.form['text']}
    if len(toot['text'] > 100):
        return 'Toot too long', 403
    basicdb.insert('toots', toot)
    return 'Toot posted'



app.run(host='0.0.0.0')