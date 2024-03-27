from PageObjects.Homepage import HomePage
from Uitility.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log=self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all product")
        products = checkoutpage.getcards()
        for product in products:
            product_name = checkoutpage.getcards_titles(product).text
            log.info(product_name)
            if 'Blackberry' == product_name:
                checkoutpage.getcard_add(product).click()
        checkoutpage.scroll_down()
        checkoutpage.checkout().click()
        cartpage = checkoutpage.checkout2()
        log.info("entering Country name as Ind")
        cartpage.countryinput().send_keys('Ind')
        self.verify_link_presence('India').click()
        #cartpage.india().click()
        cartpage.tick_checkbox().click()
        cartpage.purchased().click()
        success_text = cartpage.success_statment().text
        log.info(success_text)

        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in success_text
