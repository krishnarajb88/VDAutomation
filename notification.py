from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

import unittest

import HTMLTestRunner

class Notification(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://qa1.contus.us/products/P051/admin")
        self.driver.maximize_window()

    def test_notification(self):

        driver = self.driver
        usernameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='username']"))
        usernameFieldElement.send_keys("admin")
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='login[password]']"))
        passFieldElement.send_keys("admin123")
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@class='action-login action-primary']"))
        submitButtonElement.click()

        notiButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//a[@title='Notifications']"))
        notiButtonElement.click()

        def is_element_present(self, how, what):

            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e: return False
            return True
            self.assertTrue(self.is_element_present(By.XPATH, ".//*[@id='html-body']/div[2]/header/div[1]/div/h1"))

        # try:
        #
        #     nothButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='html-body']/div[2]/header/div[1]/div/h1"))
        #     # assert nothButtonElement.text == 'Notifications'
        #     # assert "Notifications" in self.driver.find_element_by_xpath(".//*[@id='html-body']/div[2]/header/div[1]/div/h1").text
        #     print('Notifications are displayed successfully')
        # except Exception as e:
        #     print('Notifications are not displayed', format(e))

    def tearDown(self):
            self.driver.quit()

    if __name__ == '__main__':
        HTMLTestRunner.main()
