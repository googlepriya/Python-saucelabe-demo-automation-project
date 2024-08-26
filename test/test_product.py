import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

def test_filter(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    #Login
    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")

    #Test sort the product
    sort_product =  ProductPage(driver)
    sort_product.sortProduct("Name (Z to A)")
    time.sleep(2)

    sort_product.sortProduct("Price (low to high)")
    time.sleep(2)

    sort_product.sortProduct("Price (high to low)")
    time.sleep(4)
