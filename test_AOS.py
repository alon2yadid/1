from unittest import TestCase
from qa_selenium.AOS import AOS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from openpyxl import workbook, load_workbook
excel_test_file=load_workbook(r"C:\Users\alon2\Documents\SeleniumProject.xlsx")
test_data=excel_test_file.active
test_data['C26'].value="V"
excel_test_file.save(r"C:\Users\alon2\Documents\SeleniumProject.xlsx")

class TestAOS(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Seleniumx\chromedriver.exe")
        self.driver=webdriver.Chrome(service=service_chrome)
        self.driver.get("http://www.advantageonlineshopping.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.Tester=AOS(self.driver)

    def test1(self):
        # selects 2 different products in 2 different quantities while saving the product page quantity information
        self.Tester.select_category_by_title(test_data['C2'].value)
        self.Tester.select_product(test_data['C3'].value)
        self.Tester.change_quantity(test_data['C4'].value)
        first_product_quantity=int(self.Tester.product_page_quantity())
        self.Tester.add_to_cart()

        self.Tester.back()
        self.Tester.back()

        self.Tester.select_category_by_title(test_data['C6'].value)
        self.Tester.select_product(test_data['C7'].value)
        self.Tester.change_quantity(test_data['C8'].value)
        second_product_quantity=int(self.Tester.product_page_quantity())
        self.Tester.add_to_cart()
        # cheks that the sum of the product page quantities match the amount on the shopping cart icon
        total_products_quantity=int(self.Tester.shopping_cart_icon_qty())
        self.assertEqual(total_products_quantity,(first_product_quantity+second_product_quantity))



    def test2(self):
        # selects 3 different products in 3 different quantities while saving the product page information
        self.Tester.select_category_by_title(test_data['D2'].value)
        self.Tester.select_product(test_data['D3'].value)
        self.Tester.change_quantity(test_data['D4'].value)
        first_product_name=self.Tester.product_page_name()
        first_product_quantity=self.Tester.product_page_quantity()
        first_product_color=self.Tester.product_page_color()
        first_product_price=str(float(self.Tester.product_page_price()[1:].replace(",",""))*int(first_product_quantity))
        self.Tester.add_to_cart()

        self.Tester.back()
        self.Tester.back()

        self.Tester.select_category_by_title(test_data['D6'].value)
        self.Tester.select_product(test_data['D7'].value)
        self.Tester.change_quantity(test_data['D8'].value)
        second_product_name=self.Tester.product_page_name()
        second_product_quantity=self.Tester.product_page_quantity()
        second_product_color=self.Tester.product_page_color()
        second_product_price=str(float(self.Tester.product_page_price()[1:].replace(",",""))*int(second_product_quantity))
        self.Tester.add_to_cart()

        self.Tester.back()
        self.Tester.back()

        self.Tester.select_category_by_title(test_data['D10'].value)
        self.Tester.select_product(test_data['D11'].value)
        self.Tester.change_quantity(test_data['D12'].value)
        third_product_name=self.Tester.product_page_name()
        third_product_quantity=self.Tester.product_page_quantity()
        third_product_color=self.Tester.product_page_color()
        third_product_price=str(float(self.Tester.product_page_price()[1:].replace(",",""))*int(third_product_quantity))
        self.Tester.add_to_cart()

        # checks that the product page information matches the shopping cart pop up window information
        self.assertEqual(first_product_name[0:27],self.Tester.shopping_cart_popup_product_name(3)[0:27])
        self.assertEqual(first_product_quantity,self.Tester.shopping_cart_popup_product_qty(3))
        self.assertEqual(first_product_color,self.Tester.shopping_cart_popup_product_color(3))
        self.assertEqual(first_product_price,str(float(self.Tester.shopping_cart_popup_product_price(3).replace(",","")[1:])))
        self.assertEqual(second_product_name[0:27],self.Tester.shopping_cart_popup_product_name(2)[0:27])
        self.assertEqual(second_product_quantity,self.Tester.shopping_cart_popup_product_qty(2))
        self.assertEqual(second_product_color,self.Tester.shopping_cart_popup_product_color(2))
        self.assertEqual(second_product_price,str(float(self.Tester.shopping_cart_popup_product_price(2).replace(",","")[1:])))
        self.assertEqual(third_product_name[0:27],self.Tester.shopping_cart_popup_product_name(1)[0:27])
        self.assertEqual(third_product_quantity,self.Tester.shopping_cart_popup_product_qty(1))
        self.assertEqual(third_product_color,self.Tester.shopping_cart_popup_product_color(1))
        self.assertEqual(third_product_price, str(float(self.Tester.shopping_cart_popup_product_price(1).replace(",","")[1:])))




    def test3(self):
        # selects 2 different products in 2 different quantities while saving the product names
        self.Tester.select_category_by_title(test_data['E2'].value)
        self.Tester.select_product(test_data['E3'].value)
        self.Tester.change_quantity(test_data['E4'].value)
        first_product_name = self.Tester.product_page_name()
        self.Tester.add_to_cart()

        self.Tester.back()
        self.Tester.back()

        self.Tester.select_category_by_title(test_data['E6'].value)
        self.Tester.select_product(test_data['E7'].value)
        self.Tester.change_quantity(test_data['E8'].value)
        second_product_name = self.Tester.product_page_name()
        self.Tester.add_to_cart()
        # checks that the product names saved from the product pages match the ones on the shopping cart pop up window
        # and saves the quantity on the shopping cart icon
        product_names_before=(self.Tester.shopping_cart_popup_product_name(1)[0:27],self.Tester.shopping_cart_popup_product_name(2)[0:27])
        self.assertTrue(first_product_name[0:27] and second_product_name[0:27] in product_names_before)
        quantity_before=self.Tester.shopping_cart_icon_qty()
        # removes the last product from the shopping cart pop up window
        self.Tester.shopping_cart_icon_remove_product(1)
        # checks that the product is removed by comparing the quantity on the shopping cart icon, before and after it was removed
        # checks that the product is removed by checking if the name of the product in in the product name list from the shopping cart pop up window
        quantity_after=self.Tester.shopping_cart_icon_qty()
        product_names_after=(self.Tester.shopping_cart_popup_product_name(1)[0:27], self.Tester.shopping_cart_popup_product_name(2)[0:27])
        self.assertFalse(first_product_name[0:27] and second_product_name[0:27] in product_names_after)
        self.assertNotEqual(quantity_before,quantity_after)

    def test4(self):
        # selects a product and moves to shopping cart page
        self.Tester.select_category_by_title(test_data['F2'].value)
        self.Tester.select_product(test_data['F3'].value)
        self.Tester.change_quantity(test_data['F4'].value)
        self.Tester.add_to_cart()
        self.Tester.move_to_shopping_cart_page()
        # checks that its on the shopping cart page
        self.assertEqual(self.Tester.shopping_cart_page_title(),"SHOPPING CART")

    def test5(self):
        # selects 3 different products in 3 different quantities while saving product page information
        self.Tester.select_category_by_title(test_data['G2'].value)
        self.Tester.select_product(test_data['G3'].value)
        self.Tester.change_quantity(test_data['G4'].value)
        self.Tester.add_to_cart()
        first_product_name = self.Tester.product_page_name()
        first_product_quantity = self.Tester.product_page_quantity()
        first_product_color = self.Tester.product_page_color()
        first_product_price=self.Tester.product_page_price()
        first_product=(first_product_name,first_product_quantity,first_product_color,first_product_price)

        self.Tester.back()
        self.Tester.back()

        self.Tester.select_category_by_title(test_data['G6'].value)
        self.Tester.select_product(test_data['G7'].value)
        self.Tester.change_quantity(test_data['G8'].value)
        second_product_name = self.Tester.product_page_name()
        second_product_quantity = self.Tester.product_page_quantity()
        second_product_color = self.Tester.product_page_color()
        second_product_price = self.Tester.product_page_price()
        second_product=(second_product_name,second_product_quantity,second_product_color,second_product_price)
        self.Tester.add_to_cart()

        self.Tester.back()
        self.Tester.back()

        self.Tester.select_category_by_title(test_data['G10'].value)
        self.Tester.select_product(test_data['G11'].value)
        self.Tester.change_quantity(test_data['G12'].value)
        third_product_name = self.Tester.product_page_name()
        third_product_quantity = self.Tester.product_page_quantity()
        third_product_color = self.Tester.product_page_color()
        third_product_price = self.Tester.product_page_price()
        third_product=(third_product_name,third_product_quantity,third_product_color,third_product_price)
        self.Tester.add_to_cart()
        # moves to shopping cart page and checks that the total price in page  matches the combined product prices added to cart
        self.Tester.move_to_shopping_cart_page()
        self.assertEqual(
            str(float(first_product_price.replace(",","")[1:]) * int(first_product_quantity)+float(second_product_price.replace(",","")[1:])*int(
                second_product_quantity)+float(third_product_price.replace(",","")[1:])*int(third_product_quantity)),
            str(float(self.Tester.shopping_cart_page_total_price().replace(",","")[1:])))
        # prints product name, quantity, color and price for each product
        print("product page info: ",first_product,"shopping cart page info: ",self.Tester.shopping_cart_page_info(3))
        print("product page info: ",second_product,"shopping cart page info: ",self.Tester.shopping_cart_page_info(2))
        print("product page info: ",third_product,"shopping cart page info: ",self.Tester.shopping_cart_page_info(1))

    def test6(self):
        # selects 2 different products in 2 different quantities
        self.Tester.select_category_by_title(test_data['H2'].value)
        self.Tester.select_product(test_data['H3'].value)
        self.Tester.change_quantity(test_data['H4'].value)
        first_product_quantity = self.Tester.product_page_quantity()
        self.Tester.add_to_cart()

        self.Tester.back()
        self.Tester.back()

        self.Tester.select_category_by_title(test_data['H6'].value)
        self.Tester.select_product(test_data['H7'].value)
        self.Tester.change_quantity(test_data['H8'].value)
        second_product_quantity = self.Tester.product_page_quantity()
        self.Tester.add_to_cart()
        # moves to shopping cart page and checks that the quantities in the page match the quantities that were selected
        self.Tester.move_to_shopping_cart_page()
        self.assertEqual(first_product_quantity, self.Tester.shopping_cart_page_product_qty(2))
        self.assertEqual(second_product_quantity, self.Tester.shopping_cart_page_product_qty(1))
        # edits the first product by changing the quantity and checks that the product quantity changed in the shopping cart page
        self.Tester.shopping_cart_page_edit_product(2)
        self.Tester.change_quantity(4)
        self.Tester.add_to_cart()
        self.assertNotEqual(first_product_quantity,self.Tester.shopping_cart_page_product_qty(2))
        # edits the second product by changing the quantity and checks that the product quantity changed in the shopping cart page
        self.Tester.shopping_cart_page_edit_product(1)
        self.Tester.change_quantity(1)
        self.Tester.add_to_cart()
        self.assertNotEqual(second_product_quantity,self.Tester.shopping_cart_page_product_qty(1))

    #     BUG- when editing product quantities, only the last product quantity is affected

    def test7(self):
        # selects the category tablets, checks that it's not on the home page
        # selects a products, checks that it's not on the home page and adds the product to cart
        self.Tester.select_category_by_title(test_data['I2'].value)
        self.assertTrue(self.Tester.check_if_home_page()==False)
        self.Tester.select_product(test_data['I3'].value)
        self.assertTrue(self.Tester.check_if_home_page()==False)
        self.Tester.add_to_cart()
        # moves back to the tablet category page and checks that its on it
        self.Tester.back()
        self.assertTrue(self.Tester.category_title()=="TABLETS")
        # returns to the home page and checks that its on it
        self.Tester.return_to_home_page()
        self.assertTrue(self.Tester.check_if_home_page()==True)


    def test8(self):
        # selects 3 different products in 3 different quantities and returns to home page
        self.Tester.select_category_by_title(test_data['J2'].value)
        self.Tester.select_product(test_data['J3'].value)
        self.Tester.change_quantity(test_data['J4'].value)
        self.Tester.add_to_cart()
        self.Tester.return_to_home_page()
        self.Tester.select_category_by_title(test_data['J6'].value)
        self.Tester.select_product(test_data['J7'].value)
        self.Tester.change_quantity(test_data['J8'].value)
        self.Tester.return_to_home_page()
        self.Tester.select_category_by_title(test_data['J10'].value)
        self.Tester.select_product(test_data['J11'].value)
        self.Tester.change_quantity(test_data['J12'].value)
        self.Tester.return_to_home_page()
        # moves to shopping cart page and performs checkout
        self.Tester.move_to_shopping_cart_page()
        self.Tester.checkout()
        # registers in the order payment page and creates an account
        self.Tester.order_payment_page_registration()
        self.Tester.create_account(test_data['J16'].value,test_data['J18'].value,test_data['J17'].value)
        # moves to payment section in order payment page and pays with safepay
        self.Tester.order_payment_page_click_next()
        self.Tester.order_payment_page_safe_pay(test_data['J19'].value,test_data['J20'].value)
        # checks that the shopping cart icon number is empty(no products in shopping cart)
        # and checks that the order number is in the user's order numbers list
        self.assertTrue(self.Tester.order_payment_page_payment_confirmation()==True)
        order_number=self.Tester.order_payment_page_order_number()
        self.assertTrue(self.Tester.shopping_cart_icon_qty()==0)
        self.Tester.account_icon_click()
        self.Tester.account_icon_pop_up_my_orders_click()
        self.assertTrue(order_number in self.Tester.my_orders_page_all_order_numbers())

    def test9(self):
        # selects 3 different products in 3 different quantities and returns to home page
        self.Tester.select_category_by_title(test_data['K2'].value)
        self.Tester.select_product(test_data['K3'].value)
        self.Tester.change_quantity(test_data['K4'].value)
        self.Tester.add_to_cart()
        self.Tester.return_to_home_page()
        self.Tester.select_category_by_title(test_data['K6'].value)
        self.Tester.select_product(test_data['K7'].value)
        self.Tester.change_quantity(test_data['K8'].value)
        self.Tester.return_to_home_page()
        self.Tester.select_category_by_title(test_data['K10'].value)
        self.Tester.select_product(test_data['K11'].value)
        self.Tester.change_quantity(test_data['K12'].value)
        self.Tester.return_to_home_page()
        # moves to shopping cart page and performs checkout
        self.Tester.move_to_shopping_cart_page()
        self.Tester.checkout()
        # logs in on order payment page and clicks next to move to the payment section
        self.Tester.order_payment_page_login(test_data['K14'].value,test_data['K15'].value)
        self.Tester.order_payment_page_click_next()
        # enters credit card information
        self.Tester.order_payment_page_mastercard(test_data['K21'].value.replace(",", ""),
                                                  test_data['K22'].value.replace(",", ""),
                                                  test_data['K23'].value.replace(",", ""), test_data['K24'].value,
                                                  test_data['K25'].value)
        # checks if the payment is succesfull and gets the order number
        self.assertTrue(self.Tester.order_payment_page_payment_confirmation() == True)
        order_number = self.Tester.order_payment_page_order_number()
        # checks that the shopping cart icon number is empty(no products in shopping cart)
        # and checks that the order number is in the user's order numbers list
        self.assertTrue(self.Tester.shopping_cart_icon_qty() == 0)
        self.Tester.account_icon_click()
        self.Tester.account_icon_pop_up_my_orders_click()
        self.assertTrue(order_number in self.Tester.my_orders_page_all_order_numbers())

    #   BUG- sometimes the CVV field does not recieve the first character (but recieves the rest), does not happen manually

    def test10(self):
        # checks that the user is signed out when entering the website
        self.assertTrue(self.Tester.check_if_logged_in()==False)
        # checks that the user is signed in after signing in
        self.Tester.sign_in(test_data['L14'].value,test_data['L15'].value)
        self.assertTrue(self.Tester.check_if_logged_in()==True)
        # checks that the user is signed out after signing out
        self.Tester.sign_out()
        self.assertTrue(self.Tester.check_if_logged_in() == False)

    def tearDown(self):
        sleep(0.5)
        self.Tester.return_to_home_page()
        sleep(0.5)
        self.Tester.driver.close()

# test_data['C26'].value="V"
# test_data['D26'].value="V"
# test_data['E26'].value="V"
# test_data['F26'].value="V"
# test_data['G26'].value="V"
# test_data['H26'].value="X"
# test_data['I26'].value="V"
# test_data['J26'].value="V"
# test_data['K26'].value="V"
# test_data['L26'].value="V"
