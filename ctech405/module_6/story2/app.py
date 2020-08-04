import flask
app = flask.Flask(__name__)

story = []

@app.route('/')
@app.route('/clear')
def story_start():
    global story = []
    return flask.render_template('start.html')
    
@app.route('/add')
def story_continue():
    m = request.form['new-text']
    global story.append(m)
    return flask.render_template('add.html', words = story)

app.run(host='0.0.0.0')
