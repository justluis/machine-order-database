# Working repo
Machine order generator time in so far? Tuesday start -5:30

// For this project we need to build an app that allows the user
// to create an order a purchase inquiry for GYM equiptment, focusing
// on machines. User need to be allowed to look up information by 
// using the Item number (ID machine model number) Information such as, 
// Unit Price, Description of the item, Quantity and total based on the items desired.
// User needs to be able to add, remove and update information of the items as they desire.

STEPS
1.-create database 
	*Primary key


1.- create window with Tkinker
	* Item number entry field(primary key)
	* Name 
	* Quantity to order
	* Estimated total of with Quantity selected.
2.- connect SQLite database file\
3.- print to a pdf?

WORK FLOW 
how many windows?

home window :
search bar (add placehorlder to tell user what to type)
with the primary key machine_id or name.

2 buttons 
	search and add a new entry.  

 after hitting search window:
 	shows you if there was a result on a table this windows allows user to start adding machines to a PDF(HOW?)
  check for user input mistakes
 	with the primary key machine id or name, user can either
 	search, add, delete or update machine entries to the database
	on click display the correct functionality of each button:
	
SEARCH: look it up and show it to the user, so they can know all 
	the details about the machine by name or id
    ADD: adds a new machine to the DB, display a success message? 
	DELETE: deletes the machine  given the ID 
	UPDATE: given the id update the price
	
