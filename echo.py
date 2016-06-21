
import json

import flask
Flask, request = flask.Flask, flask.request

app = Flask(__name__)

@app.route('/')
def echo():
    print request.args
    return json.dumps(request.args)

if __name__ == '__main__':
    app.run(debug=True)
