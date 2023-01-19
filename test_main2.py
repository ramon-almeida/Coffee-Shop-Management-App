from functions.menu_functions import *



def test_product_menu_options():
    expected = 1
    actual = product_menu_options()
    print(actual)
    assert expected == actual
    

def test_courier_menu_options():
    expected = 2
    actual = courier_menu_options()
    assert expected == actual
    


def test_order_menu_options():
    expected = 3
    actual = order_menu_options()
    assert expected == actual


#command to run file: pytest -s test_main2.py