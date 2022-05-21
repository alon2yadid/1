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

class Amy:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.driver.implicitly_wait(8)
        self.wait=WebDriverWait(self.driver,10)
        self.email_priority={}
        self.email_list=[]
        self.priorities=[]
        self.capacity=50


    def order_emails(self):
        ordererd_emails=sorted(self.email_priority.items(),key=lambda x:x[1],reverse=True)
        self.priority=dict(ordererd_emails)
        self.email_list=list(dict(self.priority).keys())
        self.priorities=list(dict(self.priority).values())

    def get_priority(self,something):

        a='priority'
        return a

    def get_subject(self,something):
        a=1
        return a

    def add_email(self,something):
        priority=self.get_priority(something)
        subject = self.get_subject(something)
        if len(self.email_list)<self.capacity:
            # self.emails.append(subject)
            self.email_priority[subject]=priority
            self.order_emails()

        else:
            if self.get_priority(67)>self.priorities[-1]:
                to_remove=self.email_list.pop(-1)
                del self.priority[to_remove]
                # self.emails.append(subject)
                self.email_priority[subject]=priority
                self.order_emails()



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