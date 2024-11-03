import pytest
from login_page import LoginPage
from admin_page import AdminPage

def test_admin_page_headers(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    
    admin_page = AdminPage(driver)
    assert admin_page.get_page_title() == "OrangeHRM"
    assert admin_page.is_header_present("User Management")
    assert admin_page.is_header_present("Job")
    assert admin_page.is_header_present("Organization")

def test_admin_page_menu_options(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    
    admin_page = AdminPage(driver)
    assert admin_page.is_menu_option_present("Admin")
    assert admin_page.is_menu_option_present("PIM")
    assert admin_page.is_menu_option_present("Leave")
    assert admin_page.is_menu_option_present("Time")
    assert admin_page.is_menu_option_present("Recruitment")
    assert admin_page.is_menu_option_present("My Info")
    assert admin_page.is_menu_option_present("Performance")
    assert admin_page.is_menu_option_present("Dashboard")
    assert admin_page.is_menu_option_present("Directory")
    assert admin_page.is_menu_option_present("Buzz")
    assert admin_page.is_menu_option_present("Maintenance")
