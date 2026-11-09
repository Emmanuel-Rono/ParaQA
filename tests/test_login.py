from pages.LoginPage import LoginPage

def test_login_with_valid_credentials():
    Login_page = LoginPage()
    Login_page.open_login_page()
    Login_page.enter_login_details()
    Login_page.check_login_success()
    #Assert first
    assert "Account Overview" in Login_page.check_login_success()
    Login_page.signout()
    assert "Sign in to access your account and order history." in Login_page.signout()
    
