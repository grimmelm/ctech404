import flask
app = flask.Flask(__name__)

@app.route('/')
def form_show():
    if 'message' not in request.form:
        m = '(No message yet)'
    else:
        m = request.form['message']
    return flask.render_template('form.html', msg = m)

app.run(host='0.0.0.0')
