import unittest


def product_menu_options():                                                                                                        #
    products_menu_options = " 0-Return Main Menu\n 1-Product List\n 2-Create new product\n 3-Update Product\n 4-Delete a product"  #
    print(products_menu_options)                                                                                                   #    
    option1 = int(input( "\nAnything else I can help you with? -- > "))                                                            #
    return option1  


class TestProduct_menu(unittest.TestCase):
    
     def setUp(self):
        self.user_input = 2
     
     def test_product_menu_options(self):
        
        # #Arrange
        self.assertEqual(product_menu_options, self.user_input)
        
        #Assert
        
    
    
    # def test_order_menu_options         
        
        
        


if __name__ == '__main__' :
     unittest.main()        






#python3 -m unittest test_main.py   
#pyton3 test_     