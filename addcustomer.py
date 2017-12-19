from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HTMLTestRunner

class AddCustomer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://qa1.contus.us/products/P051/admin")
        self.driver.maximize_window()

    def test_addcustomer(self):

        driver = self.driver
        usernameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='username']"))
        usernameFieldElement.send_keys("admin")
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='login[password]']"))
        passFieldElement.send_keys("admin123")
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@class='action-login action-primary']"))
        submitButtonElement.click()

        custButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("menu-magento-customer-customer"))
        custButtonElement.click()

        allcustButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='html-body']/div[3]"))
        allcustButtonElement.click()

        # addButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='add']"))
        # addButtonElement.click()

        # firstnameButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("customer[firstname]"))
        # firstnameButtonElement.send_keys("Ravi Kumar")
        #
        # lastnameButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("customer[lastname]"))
        # lastnameButtonElement.send_keys("R")
        #
        # emailButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("customer[email]"))
        # emailButtonElement.send_keys("ravikumar.r@contus.in")
        #
        # savecustButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("save"))
        # savecustButtonElement.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        HTMLTestRunner.main()