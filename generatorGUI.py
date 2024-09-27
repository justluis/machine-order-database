import tkinter, database
from tkinter import ttk
root = tkinter.Tk()
root.geometry("400x300")
root.title("Machine Order Generator")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

MENU_PROMPT= """Machine app menu 
    1) Find a Machine by ID
    2) Add a machine
    3) Show all the machines
    4) Remove a machine
    5) Update a machine
    6) Delete a machine """
#needs to have search bar, where it asks to type in either name or machine ID
#Then, it displays price, a description as well as the ablility to select quantity
# and see a total for the amount of machines the user selected *
machine_list = ["CF-3172-A","CF-3162","CF-3860","CF-3661-A","CF-3165","RPL-5403-B","RPL-5356","RS-1412"]
def search_entry():
    #if searching then show the item in the windown
    #check for user input error, compare? parse? datatype? do i want only the primary key or also the name?  to data base
    #if not found ask the user if they want to add the number or try again?s
    #print("Test")
    connection = database.connection()
    database.create_table(connection)
    input = user_input.get()

    print(input)
    #while( input != machine_list) #run while
    #if


def add_entry():
    #if adding an user_input move to window with adding information
    print("Test2")
    # compare user_input to database to see if exists in it
    #user_input = user_input.get()
    #if user_input:
    #    database.machine_list.insert(tkinter.END, user_input)
    #    #text_list.insert(tkinter.END, user_input)
    #    user_input.delete(0, tkinter.END)

#def update_entry():
    #print("Test3")


frame1= ttk.Frame(root)
frame1.grid(row=0, column=0, sticky="nsew")
frame1.columnconfigure(0,weight=1)

user_input= ttk.Entry(frame1)
user_input.grid(row=0, column=0, sticky="ew")

search_button= ttk.Button(frame1, text= "search", command= search_entry)
search_button.grid(row= 0, column= 1)

add_button=ttk.Button(frame1, text="Add Entry", command=add_entry)
add_button.grid(row=0,column=2)

#on Main windown delete button, update button, get all the machines, generate PDF button

text_list = tkinter.Listbox(frame1)

text_list.grid(row=1, column=0,columnspan=2,sticky="nsew")


root.mainloop()
