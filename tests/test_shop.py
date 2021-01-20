import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test1(BaseClass):
    def test_shop(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage= homepage.shopItems()
        log.info("getting all the card title")

        cards = checkOutPage.getCardTitles()
        for card in cards:
            ReqProduct = card.find_element_by_xpath("div/h4/a").text
            if ReqProduct == "Blackberry":
                card.find_element_by_xpath("div[2]/button").click()
        checkOutPage.getCheckOut().click()
        log.info("Checking the selected products")
        assert checkOutPage.getProductCheck().text == "Blackberry"
        confirmPage = checkOutPage.getFinalCheckOut()
        log.info("Entering country Name as ind")
        confirmPage.getLocation().send_keys("ind")
        self.VerifyingText()
        self.driver.find_element_by_xpath("//div[@class='suggestions']/ul[1]").click()
        confirmPage = ConfirmPage(self.driver)
        confirmPage.getCheckBox().click()
        confirmPage.getPurchase().click()
        Subb = confirmPage.getAlert().text
        log.info("Text received from Application is "+ Subb)
        assert "Success! Thank you!" in Subb
        self.driver.get_screenshot_as_file("screenshot.png")
