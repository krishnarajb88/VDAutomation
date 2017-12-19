from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HTMLTestRunner

class AddProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://qa1.contus.us/products/P051/admin")
        self.driver.maximize_window()

    def test_addproduct(self):

        driver = self.driver
        usernameFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@id='username']"))
        usernameFieldElement.send_keys("admin")
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='login[password]']"))
        passFieldElement.send_keys("admin123")
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//button[@class='action-login action-primary']"))
        submitButtonElement.click()

        productButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='menu-magento-catalog-catalog']/a"))
        productButtonElement.click()

        catalogButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='menu-magento-catalog-catalog']/div/ul/li/div/ul/li[1]/a"))
        catalogButtonElement.click()

        # addproductButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(".//*[@id='add_new_product-button']"))
        # addproductButtonElement.click()

        # prdctnmFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='product[name]']"))
        # prdctnmFieldElement.send_keys("Skullcandy S2DUL-J335 Headset with Mic  (Red/Black, In the Ear)")
        #
        # skuFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("//input[@name='product[sku]']"))
        # skuFieldElement.send_keys("SKU123132")
        #
        # priceFieldElement= WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("//input[@name='product[price]']"))
        # priceFieldElement.send_keys("999.99")

        # # taxFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("product[tax_class_id]"))
        # # taxFieldElement.select_by_value("0")
        #
        # qtyFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name("product[quantity_and_stock_status][qty]"))
        # qtyFieldElement.send_keys("30")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
   HTMLTestRunner.main()