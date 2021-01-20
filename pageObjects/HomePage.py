from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//ul[@class='navbar-nav']/li[2]/a")
    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.XPATH, "//input[@type='password']")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    employmentStatus = (By.ID, "inlineRadio2")
    birthday = (By.XPATH, "//input[@type='date']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    popup = (By.XPATH, "//div[@class='container']/div[2]")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
    def Name(self):
        return self.driver.find_element(*HomePage.name)
    def Email(self):
        return self.driver.find_element(*HomePage.email)
    def Password(self):
        return self.driver.find_element(*HomePage.password)
    def CheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)
    def Gender(self):
        return self.driver.find_element(*HomePage.gender)
    def EmploymentStatus(self):
        return self.driver.find_element(*HomePage.employmentStatus)
    def Birthday(self):
        return self.driver.find_element(*HomePage.birthday)
    def Submit(self):
        return self.driver.find_element(*HomePage.submit)
    def PopUp(self):
        return self.driver.find_element(*HomePage.popup)
