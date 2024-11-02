import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    assert "dashboard" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("Admin")
    login_page.enter_password("wrong_password")
    login_page.click_login()
    error_message = login_page.get_error_message()
    assert error_message == "Invalid credentials"

def test_forgot_password_link(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_forgot_password()
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.enter_username("Admin")
    forgot_password_page.click_reset_password()
    success_message = forgot_password_page.get_success_message()
    assert success_message == "Reset Password link sent successfully"
