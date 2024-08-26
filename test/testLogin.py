import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.loginPage import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")