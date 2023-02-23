# Cafe Orders System with Dockerised MySQL Database
This is a Cafe Orders System built using Python that allows you to manage products, couriers, and orders in a cafe setting. The program is equipped with a Command Line Interface (CLI) and uses a Dockerised MySQL database to store and retrieve data. The program allows you to add, view, update, and remove products, orders, and couriers.


#####   Products
- View a list of all products
- Add a new product
- Update an existing product
- Remove a product
#####  Orders
- View a list of all orders
- Add a new order
- Update an existing order
- Remove an order
- Sort orders by different attributes
##### Couriers
- View a list of all couriers
- Add a new courier
- Update an existing courier
- Remove a courier


## Data Structure
The program stores the information for products, orders, and couriers in a MySQL database. Each object is represented by a table containing the relevant attributes.

##### Products
id: integer (primary key)
name: string
price: float
##### Orders
id: integer (primary key)
name: string
address: string
telephone: string
courier: string (foreign key to couriers table)
order_status: string
order_total: float
##### Couriers
id: integer (primary key)
name: string

------------
### How to Install and Run the Project
###### Prerequisites
- Docker
- Docker Compose

###### Installation Steps
- Clone this repository to your local machine.
- Navigate to the root directory of the cloned repository.
- Run the command docker-compose up in your terminal. This will start the MySQL database and the Python program.
- Open a new terminal window and navigate to the same directory.
- Run the command docker-compose exec app python main.py to run the program.
- You can now use the CLI interface to manage products, orders, and couriers.
- Approach
- The program was built using functional programming, with each menu and submenu housed in its own function wrapper. Recursion was used to navigate between different menu functions. The program uses the MySQL connector module to interact with the Dockerised MySQL database.1.

#### Stretch and Bonus Features
Additional features added to the program include:
Sorting of orders by all attributes
Menu recursion
Deletion, updates, and addition for all object types

#### Conclusion
This program provides a CLI interface for managing products, couriers, and orders in a cafe setting. It uses a Dockerised MySQL database to store and retrieve data. The program is built using Python and follows a functional programming approach. The data structures for products, orders, and couriers are represented by MySQL tables. The program also includes several additional features, such as sorting and recursive menus.