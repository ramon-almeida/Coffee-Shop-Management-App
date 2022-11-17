
 
def product_menu_options(): 
    products_menu_options = " 0-Return Main Menu\n 1-Product List\n 2-Create new product\n 3-Update Product\n 4-Delete a product"
    print(products_menu_options)
def courier_menu_options():
    courier_menu_options = " 0-Return Main Menu\n 1-Couriers List\n 2-New courier\n 3-Update Courier\n 4-Delete a curier"
    print(courier_menu_options)
def order_menu_options():
    order_menu_options = " 0-Return Main Menu\n 1-Orders List\n 2-New Order\n 3-Update the status of an order\n 4-Update an order\n 5-Delete an order"
    print(order_menu_options)








def main_menu():
    
   main_menu = '\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '
   print(main_menu)
   while True:
    try:
      
      if main_menu_options == 0 :
       print("\n       Thank you! Have a good day")
       
    
 
      elif main_menu_options == 1:
 
       print(products_menu_options)
 
       next_option = int(input( "\nAnything else I can help you with? -- > ")) #after choosing 1 option in the initial program, we ask the user again what wants to do
    
   
       if next_option == 0:
        main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))
     
       elif next_option == 1:
        print("\n       Displaying current products...")
        with open('products.csv', 'r') as products:
         csv_dict_reader = csv.DictReader(products)
         for row in csv_dict_reader:
          print(row)
    
       elif next_option == 2:
       
        new_name = input("Please enter the name of the new product --> " )
        products_list.append(new_name)
        print("\n       Thank you, this product has been added!")
        print(products_list)
   
       
    

       elif next_option == 3:
        for i in range(len(products_list)):
         item = products_list[i]
         print(i, item)
        pick = int(input(("Select the index of the product you want to update please --> ")))
        name = (input("New product name please --> "))
        products_list[pick] = name
        print("\n       Thank you, this product has been updated!")
        print(products_list)
     
   
       elif next_option == 4:
        for i in range(len(products_list)):
         item = products_list[i]
         print(i, item) 
        choose = int(input("Please select the index of product you want to delete -- > "))
     
        products_list.pop(choose) 
        print("\n       Thank you, this product has been removed!")
        print(products_list)
    
       else:
        print("\n   Sorry, that option is not available. Try to enter the option again")
        main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))
     
 

 
      elif main_menu_options == 2:
    
       print(courier_menu_options)
    
       option2 = int(input( "\nAnything else I can help you with? -- > "))
    
       if option2 == 0:  
        main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))
    
       elif option2 == 1:
        print("\n       Displaying current curiers...")
        print(couriers_list)
    

    
       elif option2 == 2:
     
        new_courier = input("Curier name please --> ")
        couriers_list.append(new_courier)
        print("\n       Thank you, this curier has been added!")
        print(couriers_list)
     
    
       elif option2 == 3:
        for i in range(len(couriers_list)):
         item = couriers_list[i]
         print(i,item)
        choose2 = int(input("Select the index of the curier you want to update please --> "))
        name2 = input("New curier name please --> ")
        couriers_list[choose2] = name2
        print("\n       Thank you, this curier has been updated!")
        print(couriers_list)
   
    
       elif option2 == 4:
         for i in range(len(couriers_list)):
          item = couriers_list[i]
          print(i, item)
         choose3 = int(input("Select the index of the curier you want to delete please --> "))
         couriers_list.pop(choose3) 
         print("\n       Thank you, this corier has been removed!")
         print(couriers_list)
    
       else:
        print("\n   Sorry, that option is not available. Try to enter the option again")
        main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))

 

 
      elif main_menu_options == 3:
    
       print(order_menu_options)
    
       option3 = int(input( "\nAnything else I can help you with? -- > ")) #after choosing 1 option in the initial program, we ask the user again what wants to do
    
       if option3 == 0:  
        main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))
     
     
       elif option3 == 1:
        print("\n       Displaying current orders...")
        print(orders_list)
     
    
       elif option3 == 2:
      
        customer_name = input("Enter your name please: ")
        customer_address = input("Enter your address please: ")
        customer_phone = int(input("Enter your phone number please: "))
        status = "Preparing"
        orders_list.append({"customer_name": customer_name, "customer_address": customer_address, "customer_phone": customer_phone, "status": status})
        print("\n       Thank you, your order has been processed!")
        print(orders_list)
      
    
       elif option3 == 3:
        for i in range(len(orders_list)): 
         item = orders_list[i] 
         print(i, item)
         order_index = int(input("Select the index of the order you want to update please --> "))
        for (i, item2) in enumerate(order_status): # this is another way to do the above
         print(i, item2)
         status_index = int(input("What is the status of your order now? Select the index please --> "))
         orders_list[order_index]["status"] = order_status[status_index]
         print("\n       Thank you, this order has been updated!")
         print(orders_list)
       
       
       elif option3 == 4:
        for (i,item3) in enumerate(orders_list):
         print(i,item3)        
         index_dict = int(input("Select the index of the order you want to update please --> "))
       
        for (i,item4) in enumerate(orders_list[index_dict].items()):
         print(i,item4)        
         choose_key = int(input("Select the index of the product you want to update please --> "))
       
        for key,value in orders_list[choose_key]:
         orders_list[choose_key] = input("New value please --> ")
         print(orders_list)

    
    
       elif option3 == 5:
        for i in range(len(orders_list)): 
         item = orders_list[i] 
         print(i, item)
        order_index2 = int(input("Select the index of the order you want to delete please --> "))
        orders_list.pop(order_index2)
        print("\n       Thank you, this order has been removed!")
        print(orders_list)
        
    
       else:
        print("\n   Sorry, that option is not available. Try to enter the option again")
        main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))

 
 
    except ValueError:
     print("\n         Sorry, that option is not available. Please enter a number between 1-3")

 
main_menu()
 
 
 
 
 
 
 
 
 
