import database
#File to test database options 1-4
#MENU_PROMPT= """Machine app inventory...please enter an ID to look up machine..  """
MENU_PROMPT= """-----------Machine App Menu -----------
    1) Add a machine.
    2) Search and if not found ask if they want to save the machine
    3) Update a machine.
    4) Remove a machine.
    5) Show all the machines.
    6) Start an order
    7)Exit.
    Please Enter an option:"""

def menu():

    connection = database.connection()
    database.create_table(connection)
#  REMINDER...NEED TO PARSE INPUT SO REGADLESS OF UPPERCASE OR LOWERCASE ALWAYS HAS TO BE CAPITAL FOR THE FIRST 2-3 CHARS
    while( user_input := input(MENU_PROMPT))!='7':
        # Add for machine also have to see if the Machine ID already in the database otherwise
        if user_input == '1':
            machine_id = input("whats the machine ID?")
            machine_id= id_identifier(machine_id)
            add_machine(connection, machine_id)


        elif user_input == '2':#search a machine with the ID
            machine_id= input("enter machine ID")
            print(database.id_search(connection, machine_id))


        elif user_input == '3':#update needs work idk if the query is right?  #need to test
            machine_id = input("enter machine ID")
            update_machine(connection, machine_id)


        elif user_input == '4':#Remove
            machine_id = input("enter machine ID")
            delete_machine(connection,machine_id)


        elif user_input == '5':#show them all
            print(database.get_all_machines(connection))



        elif user_input == '6':#start order
            machine_id = input("enter machine ID")
            print(user_input)

        else:
            print("invalid format")

def add_machine(connection,machine_id):

    if not database.id_search(connection,machine_id) :
        name = input("Name of machine?")
        description= input("do you want to add a description")
        price = float(input("enter the price"))
        database.insert_machine(connection, machine_id, name, description, price)
        print('Machine Added succesfully!')
    else:
        print("ID already in database...Try again!")
def id_identifier(machine_id):

    #needs to check if its a CF-3165, RPL-5403-B, RS-1412

    c='-'
    parts = machine_id.split(c) #separates the id
    prefix =parts[0].upper()    #capitalizes everything beforethe dash '-'
    number_part = parts[1]

    if len(prefix) == 2 or len(prefix)==3 or len(prefix)==4:
        machine_id = prefix + c + number_part
        return machine_id
    else:
        print('Wrong ID Format')
def update_machine(connection,machine_id):
    if database.id_search(connection,machine_id):
        price = float(input("enter the price"))
        database.update_machine(connection, machine_id, price)
        print('update successful')
    else:
        print('Unable to update, ID not in database')
def delete_machine(connection, machine_id):
    if database.id_search(connection, machine_id):
        database.remove_machine(connection,machine_id)
        print('Machine Deleted Successfuly')
    else:
        print('Machine not found in the database..')
def total(connection,price):
    quantity= int(input("how many?"))
    return quantity*price

menu()
