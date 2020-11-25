# GUI based Store-Management-System-Python

This program is a store management system, this program gives you various operation like:

•	Register a product in the system

•	Billing

•	Generate sales report

•	Add shipping product to the system

•	Generate stock report

•	Exit from the program
 
Register a product

In this the program asks for the product number, product name, product description, unit price from the user after a user enters all the details, he/she needs to click on the add record button after clicking the button the program check two conditions:

•	If there is an entry present for that product number or not in the product table if it is present then it will show the error product number already added.

•	If the product number is in the shipping table or not if it is not present in that table it will show a message Product number not found.

If everything goes right the product is registered.
There is also a back button available to go back. 
 
 
Billing

In this, the user needs to enter the name and number of the customer after doing this the user can add the item to the billing list, print the list, or go back.
If the user chooses to add then the user needs to enter the product id along with the quantity if the id is correct and the quantity is less than the stock present than it is added in the billing list.

If the user clicks on print it will print the record, if there is no item present in the billing list then the print option generates error nothing to print.
There is also a back button available to go back. 
 
 
Generate sales report
In this option all the sale history is present.

There is also a back button available to go back. 
 
 
Add Shipping product to the system

In this the user needs to enter the product number, the number of units, wholesale price, and expiry date of the item after entering all the details user can click on the add record button if the user enters details correctly the record will be added.
There is also a back button available to go back. 
 
Generate stock report

In this option, all the stock can be seen on the window.
If the quantity of any item is less than 10 then their product id will be added in the order list table.
There is also a back button available to go back. 
 
Exit from the program

With the help of this option, you can close the program.
 
Software Requirement:

•	Mysql should be present 

•	Connect should be present to connect Mysql with python

•	All the necessary libraries should be pre-installed
 
How To Run This Program

To run this program you just need to change the username from root to ‘YourUsername’ and password from ’ 12345’ to ‘YourPassword’ in every place where a connection is established.

