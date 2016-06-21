
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def echo():
    return json.dumps(request.args)

if __name__ == '__main__':
    app.run(debug=True)
