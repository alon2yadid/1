from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class Amy:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.driver.implicitly_wait(8)
        self.wait=WebDriverWait(self.driver,10)
        self.email_priority_dict={}
        self.email_list=[]
        self.priorities=[]
        self.capacity=50

    def login_to_gmail(self,email,password):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#identifierId")))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ")))
        emailfield=self.driver.find_element(By.CSS_SELECTOR,"#identifierId")
        emailfield.send_keys(email)
        first_next_button=self.driver.find_element(By.CSS_SELECTOR,"button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ")
        first_next_button.click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ")))
        password_field=self.driver.find_element(By.CSS_SELECTOR,"input[name='password']")
        password_field.send_keys(password)
        second_next_button=self.driver.find_element(By.CSS_SELECTOR,"button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ")
        second_next_button.click()

    def email_contents(self,order_of_email:int):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"table[id=':26']>tbody>tr")))
        all_emails=self.driver.find_elements(By.CSS_SELECTOR,"table[id=':26']>tbody>tr")
        selected_email=all_emails[order_of_email-1]
        selected_email.click()

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h2.hP")))
        email_subject=self.driver.find_element(By.CSS_SELECTOR,"h2.hP").text

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h3.iw>span>span.gD")))
        email_sender=self.driver.find_element(By.CSS_SELECTOR,"h3.iw>span>span.gD").text

        email_priority=self.get_priority()

        self.driver.back()
        return email_subject,email_sender,email_priority


    def get_subject(self,order_of_email:int):
        email_subject=self.email_contents(order_of_email)[0]
        return email_subject

    def get_sender(self,order_of_email:int):
        email_sender=self.email_contents(order_of_email)[1]
        return email_sender

    def capital_letters_counter(self,string:str):
        count = 0
        for i in range(len(string)):
            if string[i].isupper():
                count+=1
        return count

    def priority_calculator_by_files(self,number_of_files:int):
        sum=0
        if number_of_files>0:
            for i in range(1,number_of_files+1):
                sum+=1/(2**i)
        else:
            sum=0
        return sum

    def gmail_advice(self,order_of_email:int):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"tr>td>div.pG")))
        all_emails=self.driver.find_elements(By.CSS_SELECTOR,"tr>td>div.pG")
        selected_email=all_emails[order_of_email-1]
        if selected_email.get_attribute("aria-label")=="אנחנו סבורים שההודעה הזו חשובה.":
            return 1
        else:
            return 0

    def priority_in_subject(self,subject:str):
        if 'priority:low' in subject.lower():
            return 0
        if 'priority:medium' in subject.lower():
            return 0.75
        if 'priority:high' in subject.lower():
            return 1
        else:
            return 0.5

    def get_priority(self):
        # self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table[id=':26']>tbody>tr")))
        # all_emails = self.driver.find_elements(By.CSS_SELECTOR, "table[id=':26']>tbody>tr")
        # selected_email = all_emails[order_of_email - 1]
        # selected_email.click()

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.hP")))
        email_subject=self.driver.find_element(By.CSS_SELECTOR, "h2.hP").text
        characteristic1=self.capital_letters_counter(email_subject)/len(email_subject)

        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.gs>div>div")))
        if len(self.driver.find_elements(By.CSS_SELECTOR,"div.gs>div>div"))>9:
            number_of_files_in_email=len(self.driver.find_elements(By.CSS_SELECTOR,"span.aZo"))
        else:
            number_of_files_in_email=0
        characteristic2=self.priority_calculator_by_files(number_of_files_in_email)


        characteristic3=self.priority_in_subject(email_subject)

        priority=(characteristic1+characteristic2+characteristic3)/3
        # self.driver.back()
        return priority

    def add_email(self,order_of_email:int):
        selected_email_content=self.email_contents(order_of_email)
        selected_email_subject=selected_email_content[0]
        # selected_email_sender=selected_email_content[1]
        selected_email_priority=selected_email_content[2]
        if len(self.email_list)<self.capacity:
            self.email_priority_dict[selected_email_subject]=selected_email_priority
            self.order_emails()
        else:
            if selected_email_priority>self.priorities[-1]:
                to_remove=self.email_list.pop(-1)
                del self.priority[to_remove]
                self.email_priority_dict[selected_email_subject]=selected_email_priority
                self.order_emails()


    def order_emails(self):
        ordererd_emails=sorted(self.email_priority_dict.items(),key=lambda x:x[1],reverse=True)
        self.email_priority_dict=dict(ordererd_emails)
        self.email_list=list(dict(self.email_priority_dict).keys())
        self.priorities=list(dict(self.email_priority_dict).values())


    def promotions_check(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div.aAy")))
        promotions_tab=self.driver.find_element(By.CSS_SELECTOR,"div.aAy.J-KU-KL.aJi-aLe")
        if promotions_tab.get_attribute("aria-selected")=='true':
            return True
        else:
            return False

    def primary_tab_click(self):
        if self.promotions_check()==False:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.aAy.J-KU-KL.aIf-aLe")))
            primary_tab=self.driver.find_element(By.CSS_SELECTOR,"div.aAy.J-KU-KL.aIf-aLe")
            primary_tab.click()

"span[id=':53k']>div.pG"
"אנחנו סבורים שההודעה הזו חשובה."

if __name__ == '__main__':
    service_chrome=Service(r"C:\Seleniumx\chromedriver.exe")
    amy=Amy(webdriver.Chrome(service=service_chrome))
    amy.driver.get("https://www.gmail.com")
    amy.driver.maximize_window()
    email='TesterT1387@gmail.com'
    # firstname='Tester'
    # lastname='T'
    password='TesterT11338877'
    amy.login_to_gmail(email,password)
    print(amy.get_subject(1))
    print(amy.get_sender(2))
    amy.promotions_check()
    amy.primary_tab_click()

    print(amy.add_email(2))
    print(amy.email_priority_dict.items())