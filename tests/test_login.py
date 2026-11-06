from pages.login_page import Login


def test_login_with_valid_credentials():
    login_page = Login("https://parabank.parasoft.com/parabank/lookup.htm")
    login_page.open_login_page()
    