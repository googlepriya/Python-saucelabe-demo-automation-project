from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.click_proudct_sort = (By.XPATH,"//select[@class='product_sort_container']")

        self.sauce_labs_backpack_link = (By.ID,"item_4_title_link")
        self.add_to_cart_button = (By.ID,"add-to-cart")
        self.remove_from_card = (By.ID,"remove")
        self.back_to_products = (By.ID,"back-to-products")

        self.shop_card_badge = (By.XPATH,"//span[@class='shopping_cart_badge']")
        self.checkout_button = (By.ID,"checkout")
        self.first_name_input = (By.ID,"first-name")
        self.last_name_input = (By.ID,"last-name")
        self.postal_code_input = (By.ID,"postal-code")
        self.continue_button = (By.ID,"continue")
        self.finish_button = (By.ID,"finish")

        self.back_to_home_button = (By.ID,"back-to-products")
    
    def sortProduct(self,text):
        dropdown_element = self.driver.find_element(*self.click_proudct_sort)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    def addToCart(self):
        self.driver.find_element(*self.sauce_labs_backpack_link).click()
        self.driver.find_element(*self.add_to_cart_button).click()

    def removeItem(self):
        self.driver.find_element(*self.remove_from_card).click()

    def backToProducts(self):
        self.driver.find_element(*self.back_to_products).click()

    def checkout(self,firstName, lastName, postalCode):
        self.driver.find_element(*self.shop_card_badge).click()
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(*self.first_name_input).send_keys(firstName)
        self.driver.find_element(*self.last_name_input).send_keys(lastName)
        self.driver.find_element(*self.postal_code_input).send_keys(postalCode)
        self.driver.find_element(*self.continue_button).click()
        self.driver.find_element(*self.finish_button).click()






        