import csv
import tabulate
                                                                       
                                                                                   

###################################################################################################     
def save_products():                                                                              #
    product_field = ["name",                                                                      #
                     "price"]                                                                     #
    with open('./src/products.csv', 'w') as products:                                                 #
        dict_writer = csv.DictWriter(products, fieldnames=product_field)                          #
        dict_writer.writeheader()                                                                 #
        dict_writer.writerows(products_list)                                                      #
    products.close()                                                                              #
###################################################################################################  
def save_couriers():                                                                              #
    couriers_field = ["name",                                                                     #
                      "phone_number"]                                                             #
    with open('./src/couriers.csv', 'w') as couriers:                                                 #
        dict_writer = csv.DictWriter(couriers, fieldnames=couriers_field)                         # 
        dict_writer.writeheader()                                                                 # 
        dict_writer.writerows(couriers_list)                                                      #
    couriers.close()                                                                              #
###################################################################################################  
def save_orders():                                                                                #
    orders_field = ['customer_name',                                                              #
                    'customer_address','customer_phone','status']                                 #
    with open('./src/orders.csv', 'w') as orders:                                                     #
        dict_writer = csv.DictWriter(orders, fieldnames=orders_field)                             # 
        dict_writer.writeheader()                                                                 #
        dict_writer.writerows(orders_list)                                                        #
    orders.close()                                                                                #
###################################################################################################  

def order_list_table():                                                                           #
    
    header = orders_list[0].keys()                                                                #
    rows = [i.values() for i in orders_list]                                                      #
    print(tabulate.tabulate(rows,header, tablefmt="rounded_grid"))                                #
###################################################################################################  
def product_list_table():                                                                         #
    header = products_list[0].keys()                                                              #
    rows = [i.values() for i in products_list]                                                    #
    print(tabulate.tabulate(rows, header, tablefmt="grid"))                                       #
###################################################################################################  
def courier_list_table():                                                                         #
    header = couriers_list[0].keys()                                                              #
    rows = [i.values() for i in couriers_list]                                                    #
    print(tabulate.tabulate(rows, header, tablefmt="grid"))                                       #
###################################################################################################     
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]                  #
################################################################################################### 
products_list = []                            #
with open('./src/products.csv', 'r') as products: #
  dict_reader = csv.DictReader(products)      #  
  products_list = list(dict_reader)           #  
  products.close()                            #  
###############################################
couriers_list = []                            #
with open('./src/couriers.csv', 'r') as couriers: #
  dict_reader = csv.DictReader(couriers)      #  
  couriers_list = list(dict_reader)           #  
  couriers.close()                            #  
###############################################
orders_list = []                              #
with open('./src/orders.csv', 'r') as orders:     #
  dict_reader = csv.DictReader(orders)        #
  orders_list = list(dict_reader)             #
  orders.close()                              #  
###############################################








# def options (option_list):
#  for i, item in enumerate(option_list):
#   print(f"{i} = {item}")
#   main_menu = '\n######\n¡Welcome to decentralized_exchange! \n######\n' ' 0- Exit app  /  1- Products Menu  /  2- Couriers Menu  /  3- Orders Menu'
#   print(main_menu)
#  choice = int(input("Choice"))
#  return(choice)
#  my_option = options([1,2,3,4,5])