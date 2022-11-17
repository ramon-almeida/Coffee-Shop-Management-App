products_list = ["Buy-BTC" , "Buy-ETH" , "Buy-DOT" , "Buy-Stocks"] 
couriers_list = ["John", "Ramón"]
orders_list = [{"customer_name": "John","customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334","status": "preparing"}]
orders_dict = {
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "status": "preparing"
}
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]
products_menu_options = " 0-Return Main Menu\n 1-Product List\n 2-Create new product\n 3-Update Product\n 4-Delete a product"
order_menu_options = " 0-Return Main Menu\n 1-Orders List\n 2-New Order\n 3-Update the status of an order\n 4-Update an order\n 5-Delete an order"
courier_menu_options = " 0-Return Main Menu\n 1-Couriers List\n 2-New courier\n 3-Update Courier\n 4-Delete a curier"


main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> ')) 
# get user input for main menu option


while True:  # program in bucle
 

 
 if main_menu_options == 0 :
    exit and print("\n       Thank you! Have a good day")
    break
    # close the program, go outside of the while loop to print goodbye message
    
 # products menu
 
 elif main_menu_options == 1:
 
    
    print(products_menu_options)
 
    next_option = int(input( "\nAnything else I can help you with? -- > ")) #after choosing 1 option in the initial program, we ask the user again what wants to do
    
   
    if next_option == 0:
     main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))
     # if option2 == 0: back to let the user choose again by printing the options of the main_menu

    elif next_option == 1:
     print("\n       Displaying current products...")
     print(products_list)
     
    
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
     
 
 # couriers menu
 
 elif main_menu_options == 2:
    
    print(courier_menu_options)
    
    option2 = int(input( "\nAnything else I can help you with? -- > "))
    
    if option2 == 0:  
     main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))
    
    elif option2 == 1:
     print("\n       Displaying current curiers...")
     print(couriers_list)
    
    ## New courier
    
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

 
 
 # orders menu
 
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
       for i in range(len(orders_list)): # i variable that check everything in the list
       # in is the difference between the highest and lowest values and len tells you objets inside list -- 1object,2,3 or whatever
        item = orders_list[i] # index is variable i and then each object on the list
        print(i, item)
       order_index = int(input("Select the index of the order you want to update please --> "))
       
       for (i, item2) in enumerate(order_status): # this is another way to do the above
        print(i, item2)
       status_index = int(input("What is the status of your order now? Select the index please --> "))
       orders_list[order_index]["status"] = order_status[status_index]
       # order_list(list of dicts) order_index is the index that user seleted to know which object we want to update and then the dict key
       # inside that object user selected =  index of list order_status user selected = key "status"  
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
       for i in range(len(orders_list)): # i variable that check everything in the list
       # in is the difference between the highest and lowest values and len tells you objets inside list -- 1object,2,3 or whatever
        item = orders_list[i] # index is variable i and then each object on the list
        print(i, item)
       order_index2 = int(input("Select the index of the order you want to delete please --> "))
       orders_list.pop(order_index2)
       print("\n       Thank you, this order has been removed!")
       print(orders_list)
        
    
    else:
     print("\n   Sorry, that option is not available. Try to enter the option again")
     main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))

 
 
 
 
 
 
 else:
     print("\n   Sorry, that option is not available. Try to enter the option again")
     main_menu_options = int(input('\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  --> '))
  

 
 
 
 
 

  

