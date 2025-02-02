import psycopg2

# Подключение к БД
conn = psycopg2.connect(
    dbname="mydb",
    user="dba_admin",
    password="hielhsdkjeio73902",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# cur.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         age INTEGER
#     )
# """)

# users = [("Анна", 21), ("Валерий", 27), ("Юлия", 31), ("Дмитрий", 20), ("Олег", 32)]
# cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Анна", 21))
# cur.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", users)
# cur.execute("""GRANT CREATE ON SCHEMA public TO developer;""")

# Фиксация изменений
conn.commit()

# Чтение данных
cur.execute("""SELECT * FROM users;""")
rows = cur.fetchall()
for row in rows:
    print(row)


# Закрытие соединения
cur.close()
conn.close()
