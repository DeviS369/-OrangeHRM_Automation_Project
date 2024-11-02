from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(By.NAME, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def click_forgot_password(self):
        self.driver.find_element(By.LINK_TEXT, "Forgot your password?").click()

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "error-message").text
