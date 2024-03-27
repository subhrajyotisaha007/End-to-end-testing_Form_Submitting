from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver
    shop = (By.XPATH,"//a[contains(@href,'shop')]")
    name = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    mail = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    ice_cream_checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    bday = (By.CSS_SELECTOR, "input[name='bday']")
    submit_button = (By.XPATH, "//input[@value='Submit']")
    alert_text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage
    def get_name(self):
        return self.driver.find_element(*HomePage.name)
    def get_mail(self):
        return self.driver.find_element(*HomePage.mail)
    def get_password(self):
        return self.driver.find_element(*HomePage.password)
    def get_icecream_checkbox(self):
        return self.driver.find_element(*HomePage.ice_cream_checkbox)
    def get_gender(self):
        return self.driver.find_element(*HomePage.gender_dropdown)
    def get_sumbit_button(self):
        return self.driver.find_element(*HomePage.submit_button)
    def get_alert(self):
        return self.driver.find_element(*HomePage.alert_text)
    def get_bday(self):
        return self.driver.find_element(*HomePage.bday)