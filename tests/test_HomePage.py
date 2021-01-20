import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First name is "+getData["Name"])
        homePage.Name().send_keys(getData["Name"])
        log.info("Email is "+getData["Email"])
        homePage.Email().send_keys(getData["Email"])
        log.info("Entered Password is "+getData["Password"])
        homePage.Password().send_keys(getData["Password"])
        homePage.CheckBox().click()
        log.info("Entered Gender is "+getData["gender"])
        self.SelectText(homePage.Gender(), getData["gender"])
        homePage.EmploymentStatus().click()
        log.info("Entered birthday is "+getData["birthday"])
        homePage.Birthday().send_keys(getData["birthday"])
        homePage.Submit().click()
        log.info(homePage.PopUp().text)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param