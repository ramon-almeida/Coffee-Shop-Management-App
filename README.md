######  A Cafe Order Menu System for managing products, couriers and orders in a CLI interface using Python. Client Requirements included:

- CLI navigable main menu to reach submenus for Products, Order and Courier operations
- Ability to print, add, update/amend and remove: Products, Orders, Couriers
- Commit data structures containing Product, Order and Courier information to files
- Products Attributes include: Name, Price
- Order Attributes include: Name, Address, Telephone, Items, Courier, Order Status, ID
- Courier Attributes include: Name, Orders

------------


###### Initial client requirements have been built up from products, couriers and orders represented by lists of strings saved to *.txt files, to representation using lists of dictionaries stored in csv files. Updates to the requirements provided the context for additional attributes, menu recursion and new r/w protocols. Additional Stretch and Bonus features fulfilled include:

- So far, I have created the code to meet all the requirements of creating new products, curiers and orders, and also modify each of them.
- I have also created 3 CVS files to keep the data of products, couriers and orders in these files
- If the user creates a new product, courier or order, or modifies any of these, it is automatically added to the corresponding file.


> -How did you guarantee the client requirements?

-  I have done 3 unit tests for each menu and expect input.


> If you had more time, what is one thing you would improve upon?If you had more time, what is one thing you would improve upon?

- Connect to an instance of the SQL Server Database Engine
- To create more functions to test requirements such as, adding data to CVS file and modifying them.


> -What did you most enjoy implementing?

- I really enjoyed implementing tabulate module to display list of products, couriers and orders in tablet format.
