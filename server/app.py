from flask import Flask, jsonify
import redis
import ast
import time
from db import DB
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/blogs')
def get_all_blogs():
    return jsonify([p for p in DB().get_all_blogs()])



if __name__ in '__main__':
    app.run(debug=True, port=8000)