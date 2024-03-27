from selenium.webdriver.common.by import By
from PageObjects.CartPage import CartPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    products_titles = (By.XPATH, "div/h4/a")
    products_button = (By.XPATH, "div/button")
    checkout_button = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    checkout_button2 = (By.XPATH, "//button[@class = 'btn btn-success']")


    def getcards(self):
        return self.driver.find_elements(*CheckOutPage.products)
    def getcards_titles(self,product):
        return product.find_element(*CheckOutPage.products_titles)
    def getcard_add(self,product):
        return product.find_element(*CheckOutPage.products_button)
    def scroll_down(self):
        return self.driver.execute_script('window.scrollTo(0, 0);')
    def checkout(self):
        return self.driver.find_element(*CheckOutPage.checkout_button)
    def checkout2(self):
        self.driver.find_element(*CheckOutPage.checkout_button2).click()
        cartpage = CartPage(self.driver)
        return cartpage
