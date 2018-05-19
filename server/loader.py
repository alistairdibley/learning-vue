import redis


r = redis.StrictRedis(db=8)


data = [
    {'blog1':{'title':'the big test', 'body':'We went to town'}},
    {'blog2':{'title':'the big test2', 'body':'We went to town2'}},
    {'all':{'blogs':['blog1', 'blog2']}}
]

for blog in data:
    for blog_key in blog:
        r.hmset(blog_key, blog[blog_key])


print(r.hgetall('all')[b'blogs'])