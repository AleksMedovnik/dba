import psycopg2

# Подключение к БД
conn = psycopg2.connect(
    dbname="mydb",
    user="admin",
    password="secret",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Пример запроса: создание таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")

# Добавление данных
users = [
    ("Анна", 21), ("Петр", 28), ("Инна", 20), ("Игорь", 31), ("Сергей", 21),
    ("Анна", 21), ("Ирина", 35), ("Василий", 26), ("Маргарита", 43), ("Алевтина", 41)
]
# cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Анна", 21))
cur.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", users)

# Фиксация изменений
conn.commit()

# Чтение данных
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# Закрытие соединения
cur.close()
conn.close()
