from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//div[@class='card h-100']")
    checkOut = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    productCheck = (By.XPATH, "//div[@class='media-body']/h4/a")
    finalCheckOut = (By.CSS_SELECTOR, "button[class='btn btn-success']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)
    def getCheckOut(self):
        return self.driver.find_element(*CheckOutPage.checkOut)
    def getProductCheck(self):
        return self.driver.find_element(*CheckOutPage.productCheck)
    def getFinalCheckOut(self):
        self.driver.find_element(*CheckOutPage.finalCheckOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage