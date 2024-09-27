import sqlite3
#create queries in order to use them at any time
inventory_table="CREATE TABLE IF NOT EXISTS inventory(machine_id TEXT PRIMARY KEY,name TEXT,description TEXT,quantity INT,price FLOAT,total FLOAT);"
insert_machine="INSERT INTO machines VALUES (?,?,?,?,?,?)"

#create a function that returns connection to the database provided
def connection():
    return sqlite3.connect("machine.db")

def create_table(connection):
    with connection:
        connection.execute(inventory_table)

def add_machine(connection, machine_id, name, description, quantity, price, total):
    with connection:
        connection.execute(insert_machine,(connection, machine_id, name, description, quantity, price, total))


connection().commit()
connection().close()

# def cursor():
#     return sqlite3.Cursor

# machine_list = [
#     ("CF-3163", "flat bench","pinche flat bench duh", 2, 329.45, 658.9)
#     ]

#printing the values in a table by using the cursor
#for row in cursor.execute("select * from machine_order"):
    #print(row)