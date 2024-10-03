import database
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

    while( user_input := input(MENU_PROMPT))!='7':
        if user_input == '1': #Add for machine also have to see if the Machine ID already in the database otherwise

            machine_id = input("whats the machine ID?")
            add_machine(connection, machine_id)
            exit()

        elif user_input == '2':#search a machine
            machine_id= input("enter machine ID")
            print(database.id_search(connection, machine_id))
            exit()

        elif user_input == '3':#update needs work idk if the query is right?
            machine_id = input("enter machine ID")
            update_machine(connection, machine_id)
            exit()

        elif user_input == '4':#Remove
            machine_id = input("enter machine ID")
            delete_machine(connection,machine_id)
            exit()

        elif user_input == '5':#show them all
            database.get_all_machines(connection)
            exit()


        elif user_input == '6':#start order
            machine_id = input("enter machine ID")
            print(user_input)
            exit()
        else:
            print("invalid format")

            #database.machine(connection)

def add_machine(connection,machine_id):

    name = input("Name of machine?")
    description= input("do you want to add a description")
    price = float(input("enter the price"))
    database.insert_machine(connection, machine_id, name, description, price)
def update_machine(connection,machine_id):
#check to see if the
      #name = input("Name of machine?")
      #description= input("do you want to add a description")
      price = float(input("enter the price"))
      database.update_machine(connection, machine_id, price)

def delete_machine(connection, machine_id):
    database.remove_machine(connection,machine_id)

def total(connection,price):
    quantity= int(input("how many?"))
    return quantity*price

menu()
