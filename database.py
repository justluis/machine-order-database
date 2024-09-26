import sqlite3

connection = sqlite3.connect("machine.db")
cursor = sqlite3.Cursor
with connection:
    connection.execute(
        "CREATE TABLE IF NOT EXISTS machines(machine_number TEXT PRIMARY KEY, name TEXT, description TEXT, quantity INT, price FLOAT, total FLOAT);")

machine_list = [
    ("CF-3163", "flat bench","pinche flat bench duh", 2, 329.45, 658.9)
]
connection.executemany("INSERT INTO machines VALUES (?,?,?,?,?,?)", machine_list)
#printing the values in a table by using the cursor
#for row in cursor.execute("select * from machine_order"):
    #print(row)

connection.commit()
connection.close()