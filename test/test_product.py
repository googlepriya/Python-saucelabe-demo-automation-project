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
    
    # 1. Go to Login URL
    driver.get("https://www.saucedemo.com/")

    # 2. Login
    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")

    # 3.Test sort the product
    test_product =  ProductPage(driver)
    test_product.sortProduct("Name (Z to A)")
    test_product.sortProduct("Price (low to high)")
    test_product.sortProduct("Price (high to low)")
    test_product.sortProduct("Name (A to Z)")

    # 4.Add to Cart
    test_product.addToCart()
    time.sleep(2)

    #Assrt to check item is added to the cart
    shop_card_badge = driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").text
    assert "1" in shop_card_badge, "Item is not added to the card"

    # 5.Remove item from the cart
    test_product.removeItem()
    time.sleep(2)

    #Assrt to check item is removed from the cart
    add_to_card = driver.find_element(By.ID,"add-to-cart").text
    assert "Add to cart" in add_to_card, "Item is not removed from the cart"

    # 6.Test the Back to Products
    test_product.backToProducts()
    time.sleep(2)

    # 7.Test Checkout:
    test_product.addToCart()
    time.sleep(2)

    test_product.checkout("Google","S","630900")
    time.sleep(2)

    # Assert to check Checkout the item is successfully completed
    order_success_message = driver.find_element(By.XPATH,"//h2[@class='complete-header']").text
    assert "Thank you for your order!" in order_success_message, "Checkout the item is failed"

    test_product.backToProducts()
    time.sleep(2)




    





