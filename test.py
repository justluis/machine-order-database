import database
#MENU_PROMPT= """Machine app inventory...please enter an ID to look up machine..  """
MENU_PROMPT2= """Machine app menu 
    1) Find a Machine by ID
    2) Add a machine
    3) Show all the machines
    4) Remove a machine
    5) Update a machine
    6) Delete a machine
    7) Exit
    Please Enter an option:"""
# variables to store user input
id = input("please enter machine ID")
name = input("enter name of machine")
#description = input("enter description of machine")
quantity = input("enter the quantity")

# calcualte total based on quantity

def menu():

    connection = database.connection()
    database.create_table(connection)

    while(input!=input(MENU_PROMPT2)) !=7:
        print(input)

menu()
