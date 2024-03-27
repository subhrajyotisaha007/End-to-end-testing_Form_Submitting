from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    def __init__(self,driver):
        self.driver = driver

    country_input = (By.ID, "country")
    india_tag = (By.LINK_TEXT, "India")
    check_box = (By.XPATH, "//label[@for='checkbox2']")
    purchase_button = (By.CSS_SELECTOR, "input[type = 'submit']")
    success = (By.CLASS_NAME, "alert")


    def countryinput(self):
        return self.driver.find_element(*CartPage.country_input)

    def tick_checkbox(self):
        return self.driver.find_element(*CartPage.check_box)

    def purchased(self):
        return self.driver.find_element(*CartPage.purchase_button)

    def success_statment(self):
        return self.driver.find_element(*CartPage.success)