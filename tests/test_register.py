# tests/test_register.py
from pages.RegisterPage import RegisterPage

def test_successful_user_registration():
    register_page = RegisterPage()
    register_page.open_url()
    # register_page.open_Signup_page()
    register_page.register_random_user()
    register_page.get_confirmation_message()
    # Test: check the result
    assert "Account Overview" in register_page.get_confirmation_message()