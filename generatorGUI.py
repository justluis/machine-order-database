import tkinter
from tkinter import ttk
root = tkinter.Tk()
root.geometry("400x300")
root.title("Machine Order Generator")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#needs to have search bar, where it asks to type in either name or machine ID

def search_entry():
    #if searching then show the item in the windown
    #compare entry to data base
    #if not found ask the user if they want to add the number or try again?s
   # print("Test")

    item_num = entry.get()

    #database.cursor.execute("select * from machine_order where machine_number= (?)",item_num)
    #if item_num
    #print(database.cursor.fetchall())


def add_entry():
    #if adding an entry move to window with adding information
   # print("Test2")
    # compare entry to database to see if exists in it
    item_num = entry.get()
    #if item_num:
    #    database.machine_list.insert(tkinter.END, item_num)
    #    #text_list.insert(tkinter.END, item_num)
    #    entry.delete(0, tkinter.END)

#def update_entry():
    #print("Test3")


frame1= ttk.Frame(root)
frame1.grid(row=0, column=0, sticky="nsew")
frame1.columnconfigure(0,weight=1)

entry= ttk.Entry(frame1)
entry.grid(row=0, column=0, sticky="ew")

search_button= ttk.Button(frame1, text= "search", command= search_entry)
search_button.grid(row= 0, column= 1)

add_button=ttk.Button(frame1, text="Add Entry", command=add_entry)
add_button.grid(row=0,column=2)


#delete button, update button, get all the machines, generate PDF button

text_list = tkinter.Listbox(frame1)
text_list.grid(row=1, column=0,columnspan=2,sticky="nsew")


root.mainloop()
