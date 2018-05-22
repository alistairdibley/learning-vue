from flask import (
    Flask,
    jsonify,
    request
)
import time
from db import DB
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/blogs')
def get_all_blogs():
    return jsonify([p for p in DB().get_all_blogs()])

@app.route('/blog')
def get_blog_by_id():
    b_id = request.args.get('id', default = 1, type = int)
    print([p for p in DB().get_blog_id(b_id=b_id)])
    return jsonify([p for p in DB().get_blog_id(b_id=b_id)])


if __name__ in '__main__':
    app.run(debug=True, port=8000)