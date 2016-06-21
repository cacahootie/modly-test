
import json

from flask import Flask, request

app = Flask(__name__)

print json.dumps({"bob":"dole"})

@app.route('/')
def echo():
    return json.dumps(request.args)

if __name__ == '__main__':
    app.run(debug=True)
