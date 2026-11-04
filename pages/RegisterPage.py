from helium import click, go_to, start_chrome, write, Text, S, find_all, wait_until, kill_browser
from faker import Faker

fake = Faker()
class RegisterPage():
    def __init__(self):
        self.url ="https://parabank.parasoft.com/parabank/register.htm"
         
    def open_url(self):
        start_chrome(self.url)
    
 
        
    def register_random_user(self):
        #regiseter logic
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = f"{first_name.lower()}_{fake.random_int(min=1000, max=9999)}"
        password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
        
        # Exact string labels matching ParaBank's DOM
        write(first_name, into="First Name:")
        write(last_name, into="Last Name:")
        write(fake.street_address(), into="Address:")
        write(fake.city(), into="City:")
        write(fake.state(), into="State:")
        write(fake.zipcode(), into="Zip Code:")
        write(fake.phone_number(), into="Phone #:")
        write(fake.ssn(), into="SSN:")
        write(username, into="Username:")
        write(password, into="Password:")
        write(password, into="Confirm:")
        
        click("Register")
        
        wait_until (Text("Your account was created successfully. You are now logged in.").exists, timeout_secs=10)
        
        return {"username": username, "password": password}
    
    print("RegisterPage class initialized successfully.")