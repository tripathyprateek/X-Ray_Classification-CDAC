import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

app.run(debug=True)

def btnclick():
    #Predict button click event
    pass