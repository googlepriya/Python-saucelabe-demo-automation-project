
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")


    def enterUsernme(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
    
    def enterPassword(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click() 

    def login(self, username, password):
        self.enterUsernme(username)
        self.enterPassword(password)
        self.click_login()

