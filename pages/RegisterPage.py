from helium import click, go_to, start_chrome, write, Text, S, find_all, wait_until, kill_browser
from faker import Faker

fake = Faker()
class RegisterPage():
    def __init__(self):
        self.url ="https://spree.sh/dashboard/sign-up"
         
    def open_url(self):
        start_chrome(self.url)
        
    def open_Signup_page(self):
           click("Use email") 

        
    def register_random_user(self):
        #Signup Logic
        first_name = fake.first_name()
        last_name =fake.last_name()
        #With @gmail.com
        email =fake.email(domain="gmail.com")
        password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
        write(first_name, into ="First name")
        write(last_name, into = "Last name")
        write(email, into = "Email")
        write(password, into = "password")
        click("Continue with email")
    
        
        
 
        
    def get_confirmation_message(self):
        message_locator = Text("Check your email")
        wait_until(message_locator.exists, timeout_secs=10)
        actual_message = message_locator.text
        return actual_message
        
        
        
    