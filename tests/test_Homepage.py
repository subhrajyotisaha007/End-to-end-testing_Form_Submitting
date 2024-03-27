import pytest

from PageObjects.Homepage import HomePage
from Uitility.BaseClass import BaseClass
from testData.HomepageData import HomePageData


# @pytest.mark.usefixtures("getData")
class TestHomepage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info('detail is:'+getData['Name'])
        homepage.get_name().send_keys(getData['Name'])
        homepage.get_mail().send_keys(getData['Mail'])
        homepage.get_password().send_keys("Password")
        homepage.get_icecream_checkbox().click()
        self.select_option_by_text(homepage.get_gender(),getData['Gender'])
        homepage.get_bday().send_keys("09041997")
        homepage.get_sumbit_button().click()
        alert = homepage.get_alert().text
        assert "Success! The Form has been submitted successfully!." in alert
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.get_test_data("all"))
    def getData(self,request):
        return request.param