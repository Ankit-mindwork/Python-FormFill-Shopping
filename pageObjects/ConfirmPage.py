from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    location =(By.ID, "country")
    checkBox =(By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase =(By.CSS_SELECTOR, "input[type='submit']")
    alert =(By.CLASS_NAME, "alert-success")


    def getLocation(self):
        return self.driver.find_element(*ConfirmPage.location)
    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)
    def getPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)
    def getAlert(self):
        return self.driver.find_element(*ConfirmPage.alert)
