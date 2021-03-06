import sqlite3
DB_NAME = 'blog.db'
conn = sqlite3.connect(DB_NAME)

CREATE_SQL = \
"""
CREATE TABLE IF NOT EXISTS posts (id PRIMARY KEY, 
                     date datetime default current_timestamp,
                     title text,
                     body text,
                     cat text);
"""
def create():
    cursor = conn.cursor()
    cursor.execute(CREATE_SQL)
    conn.commit()

def populate():
    cursor = conn.cursor()
    title = 'This is a blog Number: {}'
    body = 'This is some realy nice body {} Which has {}'
    for i in range(1,1000):
        cursor.execute('INSERT INTO posts (title, body) VALUES (?,?)', (title.format(i), body.format(i,i)))
    conn.commit()

class DB:

    post_keys = ['id', 'title', 'body', 'created']

    def __del__(self):
        self.conn.commit()
    
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
    
    def get_all_blogs(self):
        for post in self.cursor.execute('SELECT id, title, body, date FROM posts'):
            yield dict(zip(self.post_keys, post))
    
    def get_blog_id(self, b_id):
        for post in self.cursor.execute('SELECT id, title, body, date FROM posts WHERE id = ?', (b_id, )):
            yield dict(zip(self.post_keys, post))


if __name__ in '__main__':
    #create()
    populate()
    for i in DB().get_all_blogs():
        print(i)