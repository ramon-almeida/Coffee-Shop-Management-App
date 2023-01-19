###################################################################################################  
import traceback                                                                                  #
                                                                                                  #
from functions.savetocsv_functions import *                                                       #
from functions.menu_functions import *                                                            #
from src import *                                                                                 #
###################################################################################################





def main_menu():
    
   main_menu = '\n######\n¡Welcome to decentralized_exchange! \n######\n' 
   print(main_menu)
   
   while True:
    try:
       main_menu_options = int(input("\n0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu  -->  "))
    
            
       if main_menu_options == 0 :
        save_products()
        save_couriers()
        save_orders()
        
        print("\n       Thank you! Have a good day")
        break
       
       
       ###### -Products Menu- ######
       ######                 ######
       
       
       elif main_menu_options == 1:
        
        carry_on = True
        while carry_on == True:
                
            product_menu_selected_option = product_menu_options()
    
            
        
    
            if product_menu_selected_option == 0:
             carry_on = False
             
             
             
             
             
            elif product_menu_selected_option == 1:
             print("\n       Displaying current products...")
             product_list_table()
            
            
            
        
            elif product_menu_selected_option == 2:
        
             new_name = input("Please enter the name of the new product --> " )
             new_price = float(input("Please enter the price of the new product --> " ))
             new_product_dict = {'name': new_name, 'price': new_price}
             products_list.append(new_product_dict)
             save_products()
             print("\n       Thank you, this product has been added!")
             product_list_table()
             
            
            elif product_menu_selected_option == 3:
             for i in range(len(products_list)):
              item = products_list[i]
              print(i, item)
             
             pick = int(input(("Select the index of the product you want to update please --> ")))
             
             if pick != i:
                 print("\n   Sorry, that option is not available. Try to enter the option again")
                 
                 
             else:
                 new_name = (input("New product name please --> "))
                 new_price = float(input("Please enter the price of the product --> " ))
                 update_product_dict = {'name': new_name, 'price': new_price}
                 products_list[pick] = update_product_dict
                 save_products()
                 print("\n       Thank you, this product has been updated!")
                 product_list_table()
             
                 
            
    
            elif product_menu_selected_option == 4:
             for i in range(len(products_list)):
              item = products_list[i]
              print(i, item) 
             choose = int(input("Please select the index of product you want to delete -- > "))
             
             if choose != i:
                 print("\n   Sorry, that option is not available. Try to enter the option again")
             else:
                 
                 products_list.pop(choose) 
                 save_products()
                 print("\n       Thank you, this product has been removed!")
                 product_list_table()
            
    
            
            
            else:
                try:
                    print("\n   Sorry, that option is not available. Try to enter the option again")
                    print(main_menu)
                except:
                     traceback.print_exc()
                     print("\n   Sorry, that option is not available. Try to enter the option again")
                     print(main_menu)
                    
                    
                
 
       ###### -Couriers Menu- ######
       ######                 ######
       
       
       elif main_menu_options == 2:
           
        carry_on = True
        while carry_on == True:
            
            courier_menu_selected_option = courier_menu_options()
            
            
    
            if courier_menu_selected_option == 0:  
             carry_on = False
            
            
            elif courier_menu_selected_option == 1:
             print("\n       Displaying current curiers...")
             courier_list_table()
        

        
            elif courier_menu_selected_option == 2:
        
             new_courier = input("Name of new courier please --> ")
             courier_phone = input("Phone number of new courier please --> ")
             new_courier_dict = {'name': new_courier, 'phone_number': courier_phone}
             couriers_list.append(new_courier_dict)
             save_couriers()
             print("\n       Thank you, this curier has been added!")
             courier_list_table()
        
        
            elif courier_menu_selected_option == 3:
             for i in range(len(couriers_list)):
              item = couriers_list[i]
              print(i,item)
             choose2 = int(input("Select the index of the curier you want to update please --> "))
             
             if choose2 != i:
                 print("\n   Sorry, that option is not available. Try to enter the option again")
                 
             else:
                name2 = input("Courier name please --> ")
                phone2 = input("Courier phone number please --> ")
                update_courier_dict = {'name': name2, 'phone_number': phone2}
                couriers_list[choose2] = update_courier_dict
                save_couriers()
                print("\n       Thank you, this curier has been updated!")
                courier_list_table()
    
        
            elif courier_menu_selected_option == 4:
             for i in range(len(couriers_list)):
              item = couriers_list[i]
              print(i, item)
             choose3 = int(input("Select the index of the curier you want to delete please --> "))
             if choose3 != i:
                 print("\n   Sorry, that option is not available. Try to enter the option again")
             else:
                    
                 couriers_list.pop(choose3) 
                 save_couriers()
                 print("\n       Thank you, this corier has been removed!")
                 courier_list_table()
        
            
            else:
                try:
                    print("\n   Sorry, that option is not available. Try to enter the option again")
                    print(main_menu)
                except ValueError:
                    print("\n   Sorry, that option is not available. Try to enter the option again")
                    print(main_menu)
            

 

       ###### -Orders Menu- ######
       ######               ######
       
       
       elif main_menu_options == 3:
        
        carry_on = True
        while carry_on == True:
        
            order_menu_selected_option = order_menu_options()
        
            
        
            if order_menu_selected_option == 0:  
             carry_on = False
        
        
            elif order_menu_selected_option == 1:
             print("\n       Displaying current orders...")
             order_list_table()
        
        
            elif order_menu_selected_option == 2:
        
             customer_name = input("Enter your name please -- > ")
             customer_address = input("Enter your address please -- > ")
             customer_phone = int(input("Enter your phone number please -- > "))
             status = "Preparing"
             new_order_dict = {'customer_name': customer_name, 'customer_address': customer_address, 'customer_phone': int(customer_phone), 'status': status}
             orders_list.append(new_order_dict)
             save_orders()
             print("\n       Thank you, your order has been processed!")
             order_list_table()
        
        
            elif order_menu_selected_option == 3:
             
             for i in range(len(orders_list)): 
              item = orders_list[i] 
              print(i, item)
             order_index = int(input("Select the index of the order you want to update please --> "))
             if order_index != i:
                 print("\n   Sorry, that option is not available. Try to enter the option again")
             else:
                    
                 for (i, item2) in enumerate(order_status): 
                  print(i, item2)
                 status_index = int(input("What is the status of your order now? Select the index please --> "))
                 orders_list[order_index]["status"] = order_status[status_index]
                 save_orders()
                 print("\n       Thank you, this order has been updated!")
                 order_list_table()
             
        
            elif order_menu_selected_option == 4:
             
             for (x,item3) in enumerate(orders_list):
              print(x,item3)        
             index_dict = int(input("Select the index of the order you want to update please --> "))
             if index_dict not in range(len(orders_list)):
                 print("\n   Sorry, that option is not available. Try to enter the option again")
                 
             else:
                 
                 for (i,item4) in enumerate(orders_list[index_dict].items()):
                  print(i,item4)        
                 choose_key = int(input("Select the index of the property you want to update please  --> "))
                 if choose_key not in range(len(orders_list[index_dict])):
                     print("\n   Sorry, that option is not available. Try to enter the option again")
                 
                 elif choose_key < 0: 
                      print(" Option not available, please try again ")
                 else:     
                      if choose_key == 0:
                       key_name = input("Please enter new name --> ")
                       orders_list[index_dict]["customer_name"] = key_name
                       save_orders()
                       print("\n       Thank you, this order has been updated!")
                       order_list_table()
                      elif choose_key == 1:
                        key_address = input("Please enter new address --> ")
                        orders_list[index_dict]["customer_address"] = key_address
                        save_orders()
                        print("\n       Thank you, this order has been updated!")
                        order_list_table()
                      
                      elif choose_key == 2:
                        key_phone = input("Please enter new phone number --> ")
                        orders_list[index_dict]["customer_phone"] = key_phone
                        save_orders()
                        print("\n       Thank you, this order has been updated!")
                        order_list_table()
                      
                      elif choose_key == 3:
                          print("\n     You can update the status of this order by pressing option 3 in the menu below, please try it now :) ")
                          
                      
                      
                      else:
                        print("\n   Sorry, that option is not available. Try to enter the option again")
                         
                          
             
                   

        
        
            elif order_menu_selected_option == 5:
             for i in range(len(orders_list)): 
              item = orders_list[i] 
              print(i, item)
             order_index2 = int(input("Select the index of the order you want to delete please --> "))
             if order_index2 != i:
                 print("\n   Sorry, that option is not available. Try to enter the option again")
             else:   
                 orders_list.pop(order_index2)
                 save_orders()
                 print("\n       Thank you, this order has been updated!")
                 order_list_table()
            
        
            else:
                try:
                    print("\n   Sorry, that option is not available. Try to enter the option again")
                    print(main_menu)
                except ValueError:
                    print("\n   Sorry, that option is not available. Try to enter the option again")
                    print(main_menu)
                    

       else:
            try:
                    print("\n   Sorry, that option is not available. Try to enter the option again")
                    
            except ValueError:
                    print("\n   Sorry, that option is not available. Try1 to enter the option again")
                    
           
 
    except ValueError:
     print("\n         Sorry, that option is not available. Please try again")
     
    # except:
    #     traceback.print_exc()
   


main_menu()
 

 
