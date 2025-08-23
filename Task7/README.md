In Today,s I hve workwd on SQL and Python to  Get Basic Sales Summary from a Tiny SQLite Database using Python with the tools Python (with sqlite3, pandas, matplotlib)
 SQLite (built into Python — no setup!)
 Jupyter Notebook or a .py file.
 
 -> At first import all required libraries

 -> In next connect to a data base with help of " conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()"

-> After connecting to the data base create a table using "cursor.execute ('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT ,
        quantity INTEGER,
        price INTEGER       
    )
''') "

-> In next insert the data " sample_d = [
    ('Samsung', 10, 20),
    ('Apple', 35, 10),
    ('OnePlus', 40, 20),
    ('Xiaomi', 20, 10),
    ('Oppo', 15, 60),
    ('Vivo', 5, 90),
    ('Realme', 6, 85)
]
cursor.executemany("INSERT INTO users (product, quantity, price) VALUES (?, ?, ?)", sample_d) "

-> To retrieve the data use " cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit() "

-> Now updating "quantity" as "toatal_qty"
                " quantity*price " as "revenue
  by selecting "product" and grouping them by using " req_query = '''
SELECT product,
       SUM(quantity) As total_qty,
       SUM(quantity*price) As revenue
From users
GROUP BY product
''' "

-> Now visualizing the data and plotting " bar graphs " between " revenue by products " using " df = pd.read_sql_query(req_query, conn)
print(df)

df.plot(kind='bar', x='product', y='revenue')
plt.title('revenue by products')
plt.ylabel('revenue')
plt.xlabel('product')
plt.show()

conn.close() "

