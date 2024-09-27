import sqlite3
#create queries in order to use them at any time
INVENTORY_TABLE="CREATE TABLE IF NOT EXISTS inventory(machine_id TEXT PRIMARY KEY,name TEXT,description TEXT,quantity INT,price FLOAT,total FLOAT);"
INSERT_MACHINE="INSERT INTO machines VALUES (?,?,?,?,?,?)"
GET_ALL_MACHINES="SELECT * FROM inventory;"
NAME_LOOK_UP="SELECT * FROM inventory WHERE name=?;"
ID_LOOK_UP="SELECT * FROM inventory WHERE machine_id=?;"
DELETE_MACHINE="DELETE FROM inventory WHERE machine_id=?;"
UPDATE_MACHINE="""
    UPDATE inventory
    SET price=?
    WHERE machine_id=?;
"""

#create a function that returns connection to the database provided
def connection():
    return sqlite3.connect("machine.db")

def create_table(connection):
    with connection:
        connection.execute(INVENTORY_TABLE)

def add_machine(connection, machine_id, name, description, quantity, price, total):
    with connection:
        connection.execute(INSERT_MACHINE,(connection, machine_id, name, description, quantity, price, total))

#function that gets everything in the table
def get_all_machines(connection):
    with connection:
        return connection.execute(GET_ALL_MACHINES).fetchall()
#function looks up by machine name
def name_search(connection,name):
    with connection:
        return connection.execute(NAME_LOOK_UP,(name,)).fetchall()
#function looks up by machine id
def id_search(connection,machine_id):
    with connection:
        return connection.execute(ID_LOOK_UP,(machine_id,)).fetchall()

# function to remove a machine if needed
#needs work
def remove_machine(connection, machine_id):
    with connection:
        connection.execute(DELETE_MACHINE,(connection, machine_id))

#needs work
def update_machine(connection, machine_id, price):
    with connection:
        connection.execute(UPDATE_MACHINE,(connection, machine_id, price))

connection().commit()
connection().close()
