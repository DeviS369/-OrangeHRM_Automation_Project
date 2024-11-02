from selenium.webdriver.common.by import By

class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def is_header_present(self, header_name):
        headers = self.driver.find_elements(By.XPATH, "//h1")
        return any(header.text == header_name for header in headers)

    def is_menu_option_present(self, menu_option):
        menus = self.driver.find_elements(By.XPATH, "//ul[@class='oxd-main-menu']/li")
        return any(menu.text == menu_option for menu in menus)
