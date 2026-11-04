from helium import go_to, write, click, Text, S, find_all, wait_until, kill_browser


#login_page code

class LoginPage:
    def __init__(self, url):
        self.url = url
        return self
    
    def openUrl(self):
        go_to(self.url)
        return self
    def login(self, username, password):
        write(username, into= "Username")
        write(password, into ="Password")
        click("Login")
        wait_until(Text("Account Overview").exists, timeout_secs=10)
        return AccountPage()
        
    
     