from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.click_proudct_sort = (By.XPATH,"//select[@class='product_sort_container']")
    
    def sortProduct(self,text):
        dropdown_element = self.driver.find_element(*self.click_proudct_sort)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)


        