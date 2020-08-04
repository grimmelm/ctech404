import flask
app = flask.Flask(__name__)

story = []

@app.route('/')
def form_show():
    global story = []
    return flask.render_template('start.html')

@app.route('/add')
def form_show():
    m = request.form['new-text']
    story.append(m)
    return flask.render_template('add.html', words = story)

app.run(host='0.0.0.0')
