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

    def __init__(self):
        conn = sqlite3.connect(DB_NAME)
        self.cursor = conn.cursor()
    
    
    def get_all_blogs(self):
        for post in self.cursor.execute('SELECT id, title, body, date FROM posts'):
            yield dict(zip(self.post_keys, post))


if __name__ in '__main__':
    #reate()
    populate()
    for i in DB().get_all_blogs():
        print(i)