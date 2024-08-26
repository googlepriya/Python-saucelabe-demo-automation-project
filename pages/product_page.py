from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.click_proudct_sort = (By.XPATH,"//select[@class='product_sort_container']")

        self.sauce_labs_backpack_link = (By.ID,"item_4_title_link")
        self.add_to_cart_button = (By.ID,"add-to-cart")
        self.remove_from_card = (By.ID,"remove")
    
    def sortProduct(self,text):
        dropdown_element = self.driver.find_element(*self.click_proudct_sort)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    def addToCart(self):
        self.driver.find_element(*self.sauce_labs_backpack_link).click()
        self.driver.find_element(*self.add_to_cart_button).click()

    def removeItem(self):
        self.driver.find_element(*self.remove_from_card).click()



        