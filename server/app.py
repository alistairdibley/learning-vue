from flask import Flask, jsonify
import redis
import ast
app = Flask(__name__)
r = redis.StrictRedis(db=8, decode_responses=True)

@app.route('/')
def hello_world():
    blog_keys = r.hgetall('all')['blogs']
    all_blogs = []
    for blog_key in ast.literal_eval(blog_keys):
        print(blog_key)
        all_blogs.append(r.hgetall(blog_key))
    return jsonify(all_blogs)



if __name__ in '__main__':
    app.run(debug=True)