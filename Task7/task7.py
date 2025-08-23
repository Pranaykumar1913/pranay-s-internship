import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute ('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT ,
        quantity INTEGER,
        price INTEGER       
    )
''')
sample_d = [
    ('Samsung', 10, 20),
    ('Apple', 35, 10),
    ('OnePlus', 40, 20),
    ('Xiaomi', 20, 10),
    ('Oppo', 15, 60),
    ('Vivo', 5, 90),
    ('Realme', 6, 85)
]

cursor.executemany("INSERT INTO users (product, quantity, price) VALUES (?, ?, ?)", sample_d)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
#conn.close()

req_query = '''
SELECT product,
       SUM(quantity) As total_qty,
       SUM(quantity*price) As revenue
From users
GROUP BY product
'''
df = pd.read_sql_query(req_query, conn)
print(df)

df.plot(kind='bar', x='product', y='revenue')
plt.title('revenue by products')
plt.ylabel('revenue')
plt.xlabel('product')
plt.show()

conn.close()





