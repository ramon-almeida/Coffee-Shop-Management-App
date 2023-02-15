import unittest

def main(option1):
     while True:
        try:
            option1 = int(input("\nAnything else I can help you with? -- > "))
            return option1
        except ValueError:
            print("Invalid input: please enter an integer.")

class TestProduct_menu(unittest.TestCase):
    
    def setUp(self):
        self.user_input = 1
        
    def test_product_menu_options(self):
        # Arrange
        expected_output = 1

        
        # Act
        actual_output = main(self.user_input)
        
        # Assert
        self.assertEqual(actual_output, expected_output)
        
        
if __name__ == '__main__':
    unittest.main()


#python3 -m unittest test_main.py   
#pyton3 test_     