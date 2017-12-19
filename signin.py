from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HTMLTestRunner

class Signin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://qa1.contus.us/products/P051/admin")
        self.driver.maximize_window()

    def test_Login(self):

        driver = self.driver
        usernameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='username']"))
        usernameFieldElement.send_keys("admin")
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='login[password]']"))
        passFieldElement.send_keys("admin123")
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@class='action-login action-primary']"))
        submitButtonElement.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
   HTMLTestRunner.main()