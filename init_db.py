import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Тест-кейсы', 'Здесь находятся мои тест-кейсы')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Баг-репорты', 'Здесь находятся мои баг-репорты')
            )

connection.commit()
connection.close()
