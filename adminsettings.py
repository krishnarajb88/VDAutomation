from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HTMLTestRunner

class AdminSettings(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://qa1.contus.us/products/P051/admin")
        self.driver.maximize_window()

    def test_adminsettings(self):

        driver = self.driver
        usernameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='username']"))
        usernameFieldElement.send_keys("admin")
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='login[password]']"))
        passFieldElement.send_keys("admin123")
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@class='action-login action-primary']"))
        submitButtonElement.click()

        adminButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[@title='My Account']"))
        adminButtonElement.click()

        accstingButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[@title='Account Setting']"))
        accstingButtonElement.click()

        usrnameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='username']"))
        usrnameFieldElement.clear()
        usrnameFieldElement.send_keys("admin")
        fstnameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='firstname']"))
        fstnameFieldElement.clear()
        fstnameFieldElement.send_keys("Contus")
        lstnameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='lastname']"))
        lstnameFieldElement.clear()
        lstnameFieldElement.send_keys("Solutions")
        emilFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='email']"))
        emilFieldElement.clear()
        emilFieldElement.send_keys("sathishkumar.r@contus.in")
        vrfypwFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='current_password']"))
        vrfypwFieldElement.send_keys("admin123")

        savButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@title='Save Account']"))
        savButtonElement.click()

    def tearDown(self):
            self.driver.quit()

    if __name__ == '__main__':
        HTMLTestRunner.main()