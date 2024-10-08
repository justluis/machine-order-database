import sqlite3

import database

#create queries in order to use them at any time
INVENTORY_TABLE="CREATE TABLE IF NOT EXISTS inventory(machine_id TEXT PRIMARY KEY,name TEXT,description TEXT,price FLOAT);"
INSERT_MACHINE="INSERT INTO inventory VALUES (?,?,?,?)"
GET_ALL_MACHINES="SELECT * FROM inventory;"
NAME_LOOK_UP="SELECT * FROM inventory WHERE name=?;"
ID_LOOK_UP="SELECT * FROM inventory WHERE machine_id=?;"
DELETE_MACHINE="DELETE FROM inventory WHERE machine_id=?;"
UPDATE_MACHINE="UPDATE inventory SET name=?,description=?,price=? WHERE machine_id=?;"

#not too sure about update query need to test them

#create a function that returns connection to the database provided
def connection():
    return sqlite3.connect("machine.db")

def create_table(connection):
    with connection:
        connection.execute(INVENTORY_TABLE)

def insert_machine(connection, machine_id, name, description, price):
    with connection:
        connection.execute(INSERT_MACHINE,( machine_id, name, description, price))

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
        return connection.execute(ID_LOOK_UP, (machine_id,)).fetchall()



# function to remove a machine if needed
#needs work
def remove_machine(connection, machine_id):
    with connection:
            connection.execute(DELETE_MACHINE,(machine_id,))
#needs work
def update_machine(connection,machine_id,name,description,price):
    with connection:
        connection.execute(UPDATE_MACHINE,(name,description,price, machine_id,))

def delete_null_entries(db_name, table_name, column_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Formulate the SQL query to delete rows with NULL values in the specified column
    query = f"DELETE FROM {table_name} WHERE {column_name} IS NULL"

    try:
        # Execute the query
        cursor.execute(query)

        # Commit the changes
        conn.commit()
        print(f"Rows with NULL values in '{column_name}' have been deleted from '{table_name}'")
    except sqlite3.Error as e:
        # If an error occurs, print it
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()


# Example usage
#delete_null_entries('machine.db', 'inventory', 'machine_id')


connection().commit()
connection().close()
