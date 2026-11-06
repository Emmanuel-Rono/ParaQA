from pages.LoginPage import LoginPage

def test_login_with_valid_credentials():
    Login_page = LoginPage()
    Login_page.open_login_page()
    Login_page.enter_login_details()
    assert "Your stores" in Login_page.check_login_success()
    