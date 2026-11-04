# tests/test_register.py
from pages.RegisterPage import RegisterPage

def test_successful_user_registration():
    register_page = RegisterPage()
    register_page.open_url()
    
    credentials = register_page.register_random_user()
    
    # Assertions replace print statements in real test suites
    assert credentials["username"] != ""
    assert credentials["password"] != ""