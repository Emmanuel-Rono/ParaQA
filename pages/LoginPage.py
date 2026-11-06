import os

from helium import go_to, start_chrome, write, click, Text, S, find_all, wait_until, kill_browser
from faker import Faker

#login_page code

fake = Faker()


class LoginPage():
    def __init__(self):
        self.url = "https://spree.sh/dashboard/login"
                
    def open_login_page(self):
        start_chrome(self.url)
    
    def enter_login_details(self):
        #Login logic
        username=os.getenv("TEST_USER_EMAIL")
        password = os.getenv("TEST_USER_PASSWORD")
        
        #Write the username and password into the respective fields
        write(username, into="Email")
        write(password, into="Password")
        click("Sign in")
        
    def check_login_success(self):
        message_locator = Text("Your stores")
        wait_until(message_locator.exists, timeout_secs=10)
        actual_message = message_locator.webelement.text
        return actual_message
        
        