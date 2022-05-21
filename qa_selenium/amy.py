from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Amy:
    def __init__(self):
        self.priority={}
        self.emails=[]
        self.priorities=[]
        self.capacity=50


    def order_emails(self):
        ordererd_emails=sorted(self.priority.items(),key=lambda x:x[1],reverse=True)
        self.priority=dict(ordererd_emails)
        self.emails=list(dict(self.priority).keys())
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
        if len(self.emails)<self.capacity:
            # self.emails.append(subject)
            self.priority[subject]=priority
            self.order_emails()

        else:
            if self.get_priority(67)>self.priorities[-1]:
                to_remove=self.emails.pop(-1)
                del self.priority[to_remove]
                # self.emails.append(subject)
                self.priority[subject]=priority
                self.order_emails()








if __name__ == '__main__':
    amy=Amy()