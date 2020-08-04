import flask
app = flask.Flask(__name__)

@app.route('/form1')
def form_show():
    return flask.render_template('form1.html')

@app.route('/form2')
def form_show():
    return flask.render_template('form2.html')

@app.route('/form3')
def form_show():
    return flask.render_template('form2.html')

@app.route('/done')
def formSubmit():
    return flask.render_template('result.html', fields = flask.request.args)

app.run(host='0.0.0.0')
