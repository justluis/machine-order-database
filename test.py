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
        if user_input == '1': #Add for machine
            add_machine(connection)
            exit()

        elif user_input == '2':#search a machine
            id= input("enter machine ID")
            database.id_search(connection,id)
            print(user_input)
        elif user_input == '3':#update
            print(user_input)

        elif user_input == '4':#Remove
            print(user_input)
        elif user_input == '5':#show them all
            print(user_input)
        elif user_input == '6':#start order
            print(user_input)
        else:
            print("invalid format")

            #database.machine(connection)

def add_machine(connection):

    id = input("Machine ID?")
    name = input("Name of machine?")
    description = input("do you want to add a description")
    #quantity = int(input("Quantity desired?"))
    price = float(input("enter the price"))

    database.insert_machine(connection, id, name, description, price)

def total(connection,price):
    quantity= int(input("how many?"))
    return quantity*price

menu()
