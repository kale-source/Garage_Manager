import sqlite3 as sql


conn = sql.Connection('database/garage_controller.db')
s = conn.cursor()


model = ('Peugeot 206')
db = s.execute("DELETE FROM cars WHERE plaque = ?", ('PLD32F4',))

for rows in db:
    print(rows)

conn.commit()
conn.close()

