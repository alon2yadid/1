from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import random

class AOS:
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
        self.driver.implicitly_wait(8)

    def back(self):
        self.driver.back()

    def logo(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div[class='logo']>a[ng-click='go_up()']")

    def return_to_home_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='logo']>a[ng-click='go_up()']")))
        self.logo().click()

    def check_if_home_page(self):
        sleep(1.3)
        something=self.driver.find_element(By.CSS_SELECTOR,"body.ng-scope>div>section>article")
        if something.get_attribute("id")=="our_products":
            return True
        else:
            return False

    def category_speakers(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div[id='speakersImg']")

    def category_tablets(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div[id='tabletsImg']")

    def category_laptops(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div[id='laptopsImg']")

    def category_mice(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div[id='miceImg']")

    def category_headphones(self):
        return self.driver.find_element(By.CSS_SELECTOR,"span#headphonesTxt")

    def select_category_speakers(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#speakersTxt")))
        self.category_speakers().click()

    def select_category_tablets(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#tabletsTxt")))
        self.category_tablets().click()

    def select_category_laptops(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#laptopsTxt")))
        self.category_laptops().click()

    def select_category_mice(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#miceTxt")))
        self.category_mice().click()

    def select_category_headphones(self):
        # self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button#checkOutPopUp")))
        # use this wait when selecting more than 4 different products (pop up window blocks the headphones link)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#headphonesTxt")))
        self.category_headphones().click()

    def select_category_by_title(self,category):
        if category=="speakers":
            self.select_category_speakers()
        elif category=="tablets":
            self.select_category_tablets()
        elif category=="laptops":
            self.select_category_laptops()
        elif category=="mice":
            self.select_category_mice()
        elif category=="headphones":
            self.select_category_headphones()

    def select_random_category(self):
        categorylist=["speakers","tablets","laptops","mice","headphones"]
        random_num=random.randint(0,4)
        # if random_num==4:
            # self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button#checkOutPopUp")))
            # use this wait when selecting more than 4 different products (pop up window blocks the headphones link)
        self.select_category_by_title(categorylist[random_num])


    def category_title(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h3.categoryTitle")))
        category_title=self.driver.find_element(By.CSS_SELECTOR,"h3.categoryTitle")
        if category_title.text=="SPEAKERS":
            return "SPEAKERS"
        elif category_title.text=="TABLETS":
            return "TABLETS"
        elif category_title.text=="LAPTOPS":
            return "LAPTOPS"
        elif category_title.text=="MICE":
            return "MICE"
        elif category_title.text=="HEADPHONES":
            return "HEADPHONES"

    def products(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.roboto-medium.ng-scope")))
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li.ng-scope>img")))
        productlist=self.driver.find_elements(By.CSS_SELECTOR,"ul>li[class='ng-scope']>div[class='AddToCard']")
        return productlist

    def select_product(self,productnum:int=1):
        """enter number of product from top left to bottom right (1-number of products)"""
        # self.driver.implicitly_wait(8)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.titleItemsCount")))
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ng-scope>img")))
        numberofitemsinpage = self.driver.find_element(By.CSS_SELECTOR, "a.titleItemsCount")
        if int(numberofitemsinpage.text.split()[0]) < productnum:
            productnum = len(self.products())
        productlist = self.products()
        product = productlist[productnum-1]
        # self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button#checkOutPopUp")))
        # use this wait when selecting more than 4 different products (pop up window blocks the link)
        product.click()

    def select_random_product(self):
        productlist=self.products()
        randomnum=random.randint(0,len(productlist)-1)
        product=productlist[randomnum]
        # self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button#checkOutPopUp")))
        # use this wait when selecting more than 4 different products (pop up window blocks the link)
        product.click()

    def select_product_by_id(self,id:int):
        id=str(id)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.titleItemsCount")))
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ng-scope>img")))
        product=self.driver.find_element(By.CSS_SELECTOR,f"[id='{id}']")
        product.click()

    def add_to_cart_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"button[name='save_to_cart']")

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='save_to_cart']")))
        self.add_to_cart_button().click()

    def add_quantity_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div[class='plus']")

    def reduce_quantity_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"div[class='minus']")

    def add_quantity(self,num:int=1):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='plus']")))
        for i in range(num):
            self.add_quantity_button().click()

    def reduce_quantity(self,num:int=1):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='minus']")))
        for i in range(num):
            self.reduce_quantity_button().click()

    def change_quantity(self,num:int):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='quantity'][ng-model='numAttr']")))
        quantity = self.driver.find_element(By.CSS_SELECTOR, "input[name='quantity'][ng-model='numAttr']")
        for i in range(5):
            quantity.send_keys(Keys.BACK_SPACE)
        quantity.send_keys(num)

    def product_page_name(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.roboto-regular.screen768")))
        name=self.driver.find_element(By.CSS_SELECTOR,"h1.roboto-regular.screen768")
        return name.text

    def product_page_price(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div#Description>h2.roboto-thin.screen768.ng-binding")))
        price=self.driver.find_element(By.CSS_SELECTOR,"div#Description>h2.roboto-thin.screen768.ng-binding")
        return price.text

    def product_page_quantity(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='quantity'][ng-model='numAttr']")))
        quantity=self.driver.find_element(By.CSS_SELECTOR,"input[name='quantity'][ng-model='numAttr']")
        return quantity.get_attribute("value")

    def product_page_color(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[ng-if='product.colors.length > 0']>div[class='']>span.colorSelected")))
        color=self.driver.find_element(By.CSS_SELECTOR,"div[ng-if='product.colors.length > 0']>div[class='']>span.colorSelected")
        return color.get_attribute("title")

    def product_page_info(self):
        name=self.product_page_name()
        quantity=self.product_page_quantity()
        color=self.product_page_color()
        price=self.product_page_price()
        return name[0:27],quantity,color,price

    def shopping_cart_icon(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shoppingCartLink")))
        shoppingcarticon=self.driver.find_element(By.CSS_SELECTOR,"#shoppingCartLink")
        return shoppingcarticon

    def shopping_cart_icon_qty(self):
        sleep(1)
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"a[id='shoppingCartLink']")))
        a=self.driver.find_elements(By.CSS_SELECTOR,"span.cart.ng-binding")
        b=a[-1]
        if b.text=="":
            return 0
        else:
            return b.text

    def shopping_cart_popup_product_info(self,productorder:int=1):
        hover=ActionChains(self.driver).move_to_element(self.driver.find_element(By.CSS_SELECTOR,"#menuCart > path:nth-child(1)"))
        hover.perform()
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"li>tool-tip-cart>div>table")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button#checkOutPopUp")))
        products_names=self.driver.find_elements(By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tbody>tr>td>a>h3")
        products_colors_qty=self.driver.find_elements(By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tbody>tr>td>a>label")
        products_prices=self.driver.find_elements(By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tbody>tr>td>p")
        if productorder>len(products_names):
            productorder=len(products_names)
        return products_names[productorder-1].text,products_colors_qty[(2*productorder-2)].text.split()[-1],products_colors_qty[(2*productorder-1)].text.split()[-1],products_prices[(productorder-1)].text

    def shopping_cart_popup_product_name(self,productorder:int=1):
        productname=self.shopping_cart_popup_product_info(productorder)[0]
        return productname

    def shopping_cart_popup_product_qty(self,productorder:int=1):
        productqty=self.shopping_cart_popup_product_info(productorder)[1]
        return productqty

    def shopping_cart_popup_product_color(self,productorder:int=1):
        productcolor=self.shopping_cart_popup_product_info(productorder)[2]
        return productcolor

    def shopping_cart_popup_product_price(self,productorder:int=1):
        productprice=self.shopping_cart_popup_product_info(productorder)[3]
        return productprice

    def shopping_cart_icon_remove_product(self,productorderinpopup:int=1):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(By.CSS_SELECTOR, "svg#menuCart>path[fill='#313131']"))
        hover.perform()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"table>tbody>tr>td>div>div.removeProduct")))
        removebuttons=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>div>div.removeProduct")
        if productorderinpopup>len(removebuttons):
            selected_remove_button=removebuttons[len(removebuttons)-1]
        else:
            selected_remove_button=removebuttons[productorderinpopup-1]
        selected_remove_button.click()

    def move_to_shopping_cart_page(self):
        self.shopping_cart_icon().click()

    def shopping_cart_page_title(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"h3.roboto-regular.sticky")))
        page_title=self.driver.find_element(By.CSS_SELECTOR,"h3.roboto-regular.sticky").text
        return page_title.split()[0]+" "+page_title.split()[1]

    def shopping_cart_page_info(self,productorderinpage:int=1):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "h3.roboto-regular.sticky")))
        allproductsnames=self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td>label.roboto-regular.productName")
        allproductscolors=self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td>span.productColor")
        allproductqtys=self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td.smollCell.quantityMobile>label.ng-binding")
        allproductsprices=self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td.smollCell>p")
        if productorderinpage>len(allproductsnames):
            productorderinpage=len(allproductsnames)
        productname=allproductsnames[productorderinpage-1]
        productcolor=allproductscolors[productorderinpage-1]
        productquantity=allproductqtys[productorderinpage-1]
        productprice=allproductsprices[productorderinpage-1]
        return productname.text,productquantity.text,productcolor.get_attribute("title"),productprice.text

    def shopping_cart_page_product_name(self,productorderinpage:int=1):
        return self.shopping_cart_page_info(productorderinpage)[0]

    def shopping_cart_page_product_qty(self, productorderinpage: int = 1):
        return self.shopping_cart_page_info(productorderinpage)[1]

    def shopping_cart_page_product_color(self,productorderinpage:int=1):
        return self.shopping_cart_page_info(productorderinpage)[2]

    def shopping_cart_page_product_price(self,productorderinpage:int=1):
        return self.shopping_cart_page_info(productorderinpage)[3]

    def shopping_cart_page_total_price(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"td[colspan='2']")))
        total=self.driver.find_element(By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tfoot>tr>td>span.roboto-medium.cart-total")
        return total.text

    def shopping_cart_page_edit_product(self,orderofproduct:int=1):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table>tbody>tr>td>span")))
        self.wait.until_not(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tbody>tr>td>a>h3")))
        editbuttons=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>span>a.edit")
        if orderofproduct>len(editbuttons):
            orderofproduct=len(editbuttons)
        editb=editbuttons[orderofproduct-1]
        editb.click()

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#checkOutButton")))
        checkoutbutton=self.driver.find_element(By.CSS_SELECTOR,"button#checkOutButton")
        checkoutbutton.click()

    def order_payment_page_username_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='usernameInOrderPayment'][type='text']")

    def order_payment_page_enter_username(self,username):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='usernameInOrderPayment'][type='text']")))
        usernamefield=self.order_payment_page_username_field()
        usernamefield.send_keys(username)

    def order_payment_page_password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR,"input[name='passwordInOrderPayment'][type='password']")

    def order_payment_page_enter_password(self,password):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='passwordInOrderPayment'][type='password']")))
        passwordfield=self.order_payment_page_password_field()
        passwordfield.send_keys(password)

    def order_payment_page_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"button#login_btnundefined")

    def order_payment_page_click_login(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#login_btnundefined")))
        loginbutton=self.order_payment_page_login_button()
        loginbutton.click()

    def order_payment_page_login(self,username,password):
        self.order_payment_page_enter_username(username)
        self.order_payment_page_enter_password(password)
        self.order_payment_page_click_login()

    def order_payment_page_registration_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"button#registration_btnundefined")

    def order_payment_page_registration(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#registration_btnundefined")))
        registrationbutton=self.order_payment_page_registration_button()
        registrationbutton.click()

    def create_account_page_username_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='usernameRegisterPage']")

    def create_account_page_enter_username(self,username):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='usernameRegisterPage']")))
        usernamefield=self.create_account_page_username_field()
        usernamefield.send_keys(username)

    def create_account_page_password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='passwordRegisterPage']")

    def create_account_page_enter_password(self,password):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='passwordRegisterPage']")))
        passwordfield= self.create_account_page_password_field()
        passwordfield.send_keys(password)

    def create_account_page_confirm_password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='confirm_passwordRegisterPage']")

    def create_account_page_confirm_password(self,password):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='confirm_passwordRegisterPage']")))
        confirmpasswordfield=self.create_account_page_confirm_password_field()
        confirmpasswordfield.send_keys(password)

    def create_account_page_email_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='emailRegisterPage']")

    def create_account_page_enter_email(self,email):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='emailRegisterPage']")))
        emailfield=self.create_account_page_email_field()
        emailfield.send_keys(email)

    def create_account_page_conditions_check(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']")

    def create_account_page_click_on_conditions(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='i_agree']")))
        AOS_condtions_check=self.create_account_page_conditions_check()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ALREADY_HAVE_AN_ACCOUNT")))
        AOS_condtions_check.click()

    def create_account_page_register_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button#register_btnundefined")

    def create_account_page_click_register(self):
        # sleep(0.5)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#register_btnundefined")))
        registerbutton=self.create_account_page_register_button()
        # self.driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.CONTROL, Keys.END)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ALREADY_HAVE_AN_ACCOUNT")))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#register_btnundefined")))
        if registerbutton.is_displayed():
            registerbutton.click()

    def create_account(self,username,password,email):
        self.create_account_page_enter_username(username)
        self.create_account_page_enter_password(password)
        self.create_account_page_confirm_password(password)
        self.create_account_page_enter_email(email)
        self.create_account_page_click_on_conditions()
        self.create_account_page_click_register()

    def order_payment_page_next_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"button#next_btn")

    def order_payment_page_click_next(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#next_btn")))
        next_button=self.order_payment_page_next_button()
        next_button.click()

    def order_payment_page_safe_pay(self,username,password):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='safepay']")))
        safepay_check=self.driver.find_element(By.CSS_SELECTOR,"input[name='safepay']")
        if safepay_check.get_attribute("checked")!="true":
            safepay_check.click()
        safepay_username=self.driver.find_element(By.CSS_SELECTOR,"input[name='safepay_username']")
        safepay_password=self.driver.find_element(By.CSS_SELECTOR,"input[name='safepay_password']")
        safepay_username.clear()
        safepay_password.clear()
        safepay_username.send_keys(username)
        safepay_password.send_keys(password)
        # save_changes_check=self.driver.find_element(By.CSS_SELECTOR,"input[name='save-safepay']")
        # save_changes_check.click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#pay_now_btn_SAFEPAY")))
        pay_now_button=self.driver.find_element(By.CSS_SELECTOR,"button#pay_now_btn_SAFEPAY")
        pay_now_button.click()

    def order_payment_page_mastercard(self,card_number,CVV,MM,YYYY,cardholder_name):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='masterCredit']")))
        mastercredit_check=self.driver.find_element(By.CSS_SELECTOR,"input[name='masterCredit']")
        if mastercredit_check.get_attribute("checked")!="true":
            mastercredit_check.click()

        # if the website saved credit payment information:
        first_pay_now_button=self.driver.find_element(By.CSS_SELECTOR,"button#pay_now_btn_ManualPayment")
        if first_pay_now_button.is_displayed()==False:
            # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#pay_now_btn_MasterCredit")))
            # second_pay_now_button=self.driver.find_element(By.CSS_SELECTOR,"button#pay_now_btn_MasterCredit")
            # second_pay_now_button.click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"label.edit[data-ng-click='toggleShowMasterCart()']")))
            edit_button=self.driver.find_element(By.CSS_SELECTOR,"label.edit[data-ng-click='toggleShowMasterCart()']")
            edit_button.click()

            card_number_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='card_number']")
            card_number_field.clear()
            card_number_field.send_keys(card_number)

            CVV_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cvv_number']")
            CVV_field.clear()
            CVV_field.send_keys(CVV)

            cardholder_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='cardholder_name']")
            cardholder_name_field.clear()
            cardholder_name_field.send_keys(cardholder_name)

            year = self.driver.find_element(By.CSS_SELECTOR, "select[name=yyyyListbox]")
            # year_dropdown=Select(year)
            # year_dropdown.select_by_visible_text(YYYY)
            year.click()
            self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"select[name=yyyyListbox]>option[label='{YYYY}']")))
            selected_year = self.driver.find_element(By.CSS_SELECTOR,
                                                     f"select[name=yyyyListbox]>option[label='{YYYY}']")
            selected_year.click()

            month = self.driver.find_element(By.CSS_SELECTOR, "select[name=mmListbox]")
            # month_dropdown=Select(month)
            # month_dropdown.select_by_visible_text(MM)
            month.click()
            self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"select[name=mmListbox]>option[label='{MM}']")))
            selected_month = self.driver.find_element(By.CSS_SELECTOR, f"select[name=mmListbox]>option[label='{MM}']")
            selected_month.click()
            if len(CVV_field.get_attribute("value"))<3:
                for i in range(4):
                    CVV_field.send_keys(Keys.BACK_SPACE)
                CVV_field.send_keys(CVV[0],CVV[1],CVV[2])

            # save_changes_check=self.driver.find_element(By.CSS_SELECTOR,"input[name='save-safepay']")
            # save_changes_check.click()
            first_pay_now_button.click()

        # if the website did not save credit payment information
        else:
            card_number_field=self.driver.find_element(By.CSS_SELECTOR,"input[name='card_number']")
            card_number_field.clear()
            card_number_field.send_keys(card_number)

            CVV_field=self.driver.find_element(By.CSS_SELECTOR,"input[name='cvv_number']")
            CVV_field.clear()
            CVV_field.send_keys(CVV)

            cardholder_name_field=self.driver.find_element(By.CSS_SELECTOR,"input[name='cardholder_name']")
            cardholder_name_field.clear()
            cardholder_name_field.send_keys(cardholder_name)

            year=self.driver.find_element(By.CSS_SELECTOR,"select[name=yyyyListbox]")
            # year_dropdown=Select(year)
            # year_dropdown.select_by_visible_text(YYYY)
            year.click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"select[name=yyyyListbox]>option[label='{YYYY}']")))
            selected_year=self.driver.find_element(By.CSS_SELECTOR, f"select[name=yyyyListbox]>option[label='{YYYY}']")
            selected_year.click()

            month=self.driver.find_element(By.CSS_SELECTOR,"select[name=mmListbox]")
            # month_dropdown=Select(month)
            # month_dropdown.select_by_visible_text(MM)
            month.click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"select[name=mmListbox]>option[label='{MM}']")))
            selected_month=self.driver.find_element(By.CSS_SELECTOR,f"select[name=mmListbox]>option[label='{MM}']")
            selected_month.click()

            if len(CVV_field.get_attribute("value"))<3:
                for i in range(4):
                    CVV_field.send_keys(Keys.BACK_SPACE)
                CVV_field.send_keys(CVV[0],CVV[1],CVV[2])
            # save_changes_check=self.driver.find_element(By.CSS_SELECTOR,"input[name='save-safepay']")
            # save_changes_check.click()
            first_pay_now_button.click()

    def order_payment_page_payment_confirmation(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div>div>h2>span.roboto-regular.ng-scope")))
        payment_confirmation_message=self.driver.find_element(By.CSS_SELECTOR,"div>div>h2>span.roboto-regular.ng-scope")
        if payment_confirmation_message.text=="Thank you for buying with Advantage":
            return True

    def order_payment_page_order_number(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div>div>h2>span.roboto-regular.ng-scope")))
        order_number=self.driver.find_element(By.CSS_SELECTOR,"label#orderNumberLabel")
        return order_number.text

    def account_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR,"svg#menuUser")

    def account_icon_user_name(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"header>nav>ul>li>a>span.hi-user")))
        user_name=self.driver.find_element(By.CSS_SELECTOR,"header>nav>ul>li>a>span.hi-user")
        return user_name.text

    def check_if_logged_in(self):
        sleep(4)
        username=self.account_icon_user_name()
        if username!="":
            return True
        else:
            return False

    def account_icon_click(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg#menuUser")))
        account_icon=self.account_icon()
        account_icon.click()

    def account_icon_pop_up_my_orders(self):
        return self.driver.find_element(By.CSS_SELECTOR,"a#menuUserLink>div>label[translate='My_Orders']")

    def account_icon_pop_up_my_orders_click(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#menuUserLink>div>label[translate='My_Orders']")))
        my_orders_page_link=self.account_icon_pop_up_my_orders()
        my_orders_page_link.click()

    def account_icon_pop_up_sign_out(self):
        return self.driver.find_element(By.CSS_SELECTOR,"label.option[ng-click='signOut($event)']")

    def account_icon_pop_up_sign_out_click(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label.option[ng-click='signOut($event)']")))
        sign_out_link=self.account_icon_pop_up_sign_out()
        sign_out_link.click()

    def sign_out(self):
        self.account_icon_click()
        self.account_icon_pop_up_sign_out_click()


    def my_orders_page_all_order_numbers(self):
        order_numbers_list=[]
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div>table>tbody>tr")))
        all_orders_info=self.driver.find_elements(By.CSS_SELECTOR,"tr[data-ng-repeat-start='order in myOrdersCtrl.orders track by $index']>td")
        for i in range(int(len(all_orders_info)/7)):
            order_number=self.driver.find_elements(By.CSS_SELECTOR,"tr[data-ng-repeat-start='order in myOrdersCtrl.orders track by $index']>td")[i*7]
            order_numbers_list.append(order_number.text)
        return order_numbers_list

    def my_order_page_get_order_number(self,order_of_order:int=1):
        all_orders_numbers=self.my_orders_page_all_order_numbers()
        if order_of_order>len(all_orders_numbers):
            order_of_order=len(all_orders_numbers)
        return all_orders_numbers[order_of_order-1]

    def my_order_page_check_if_ordernumber_in_list(self,ordernumber):
        all_orders_numbers = self.my_orders_page_all_order_numbers()
        if str(ordernumber) in all_orders_numbers:
            return True
        else:
            return False

    def sign_in_pop_up_username_field(self):
        return self.driver.find_element(By.CSS_SELECTOR,"input[name='username']")

    def sign_in_pop_up_enter_username(self,username):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        username_field=self.sign_in_pop_up_username_field()
        username_field.send_keys(username)

    def sign_in_pop_up_password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR,"input[name='password']")

    def sign_in_pop_up_enter_password(self,password):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        password_field=self.sign_in_pop_up_password_field()
        password_field.send_keys(password)

    def sign_in_pop_up_sign_in_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"button#sign_in_btnundefined")

    def sign_in_pop_up_sign_in_click(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#sign_in_btnundefined")))
        sign_in_button=self.sign_in_pop_up_sign_in_button()
        sign_in_button.click()

    def sign_in(self,username,password):
        self.account_icon_click()
        self.sign_in_pop_up_enter_username(username)
        self.sign_in_pop_up_enter_password(password)
        sleep(1)
        self.sign_in_pop_up_sign_in_click()





