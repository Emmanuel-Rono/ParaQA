import os
from helium import click, go_to, start_chrome, write, Text, S, find_all, wait_until, kill_browser
from faker import Faker

fake = Faker()
class RegisterPage():
    def __init__(self):
        self.url ="https://demo.spreecommerce.org/us/en/account/register"
         
    def open_url(self):
        start_chrome(self.url)
        
    #def open_Signup_page(self):
           #click("Use email") 

        
    def register_random_user(self):
        #Signup Logic
        first_name = fake.first_name()
        last_name =fake.last_name()
        #With @gmail.com
        email = os.getenv("TEST_USER_EMAIL")
        password = os.getenv("TEST_USER_PASSWORD")
        write(first_name, into ="First name")
        write(last_name, into = "Last name")
        write(email, into = "Email")
        write(password, into = "password")
        write(password, into = "Confirm password")
        click("I agree to the Privacy Policy and Terms of Service")
        click("Create Account")
    
    def get_confirmation_message(self):
        message_locator = Text("Account Overview")
        wait_until(message_locator.exists, timeout_secs=10)
        actual_message = message_locator.web_element.text
        return actual_message
        
        
        
    