######  A Cafe Order Menu System for managing products, couriers and orders in a CLI interface using Python. Client Requirements included:

- CLI navigable main menu to reach submenus for Products, Order and Courier operations
- Ability to print, add, update/amend and remove: Products, Orders, Couriers
- Commit data structures containing Product, Order and Courier information to files
- Products Attributes include: Name, Price
- Order Attributes include: Name, Address, Telephone, Items, Courier, Order Status, ID
- Courier Attributes include: Name, Orders

------------


###### Initial client requirements have been built up from products, couriers and orders represented by lists of strings saved to *.txt files, to representation using lists of dictionaries stored in csv files. Updates to the requirements provided the context for additional attributes, menu recursion and new r/w protocols. Additional Stretch and Bonus features fulfilled include:

- Sorting of Orders List by all attributes
- Menu Recursion
- Deletion, Updates, Addition for all object types
- To achieve this, the approach follows Functional Programming, with each menu and submenu housed in it's own def function wrapper with recursion to navigate between different menu function

