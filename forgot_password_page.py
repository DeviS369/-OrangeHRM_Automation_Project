from selenium.webdriver.common.by import By

class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, "username").send_keys(username)

    def click_reset_password(self):
        self.driver.find_element(By.XPATH, "//button[text()='Reset Password']").click()

    def get_success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "success-message").text
