from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HTMLTestRunner

class AddStore(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://qa1.contus.us/products/P051/admin")
        self.driver.maximize_window()

    def test_Addstore(self):

        driver = self.driver
        usernameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='username']"))
        usernameFieldElement.send_keys("admin")
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='login[password]']"))
        passFieldElement.send_keys("admin123")
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@class='action-login action-primary']"))
        submitButtonElement.click()

        storeButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='menu-magento-backend-stores']/a"))
        storeButtonElement.click()
        allstoreButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("All Stores"))
        allstoreButtonElement.click()
        createstoreButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='add_group']"))
        createstoreButtonElement.click()
        storenameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='group_name']"))
        storenameFieldElement.send_keys("Mystore")

        el = driver.find_element_by_id("group_root_category_id")
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'Default Category':
                option.click()  #

    # def select_dropdown_option(driver, select_locator, option_text):
    #     dropdown = driver.find_element_by_xpath(".//*[@id='group_root_category_id']")
    #     driver.select_dropdown_option(driver, dropdown, "Option 2")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
   HTMLTestRunner.main()