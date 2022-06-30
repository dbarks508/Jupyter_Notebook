import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

conn.execute('''CREATE TABLE books
     (title VARCHAR(20) PRIMARY KEY,
      author VARCHAR(20),
      year INT)''')

ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'
conn.execute(ins, 'Sapiens', 'Yuval Noah Harari', 2015)
conn.execute(ins, 'Mans Search for Meaning', 'Victor E. Frankl', 1959)
conn.execute(ins, 'Mindfulness for Beginners', 'Jon Kabat-Zinn', 2000.0)

rows = conn.execute('SELECT title FROM books')

for row in rows:
    print(row) 