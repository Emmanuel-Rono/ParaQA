from helium import go_to, start_chrome, write, click, Text, S, find_all, wait_until, kill_browser
from faker import Faker

#login_page code

fake = Faker()

class Login:
    def __init__(self,url):
        self.url = url
                
    def open_login_page(self):
        start_chrome(self.url)
    
    def Login(self):
        #Login logic
        username= 
        password =fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
        
        #Write the username and password into the respective fields
        write(username, into="Username:")
        write(password, into="Password:")
        click("Log In")
        wait_until(Text("Welcome").exists, timeout_secs=10)
        