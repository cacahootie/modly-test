
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo')
def echo():
    return jsonify(request.args)

if __name__ == '__main__':
    app.run(debug=True)
