import os
import unittest
import HTMLTestRunner
import signin
import addproduct
import addcustomer
import adminsettings
import notification
import addstore
import time


dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
signin = unittest.TestLoader().loadTestsFromTestCase(signin.Signin)
addproduct = unittest.TestLoader().loadTestsFromTestCase(addproduct.AddProduct)
addcustomer = unittest.TestLoader().loadTestsFromTestCase(addcustomer.AddCustomer)
adminsettings = unittest.TestLoader().loadTestsFromTestCase(adminsettings.AdminSettings)
notification = unittest.TestLoader().loadTestsFromTestCase(notification.Notification)
addstore = unittest.TestLoader().loadTestsFromTestCase(addstore.AddStore)
time.sleep(5)
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([signin,addproduct,addcustomer,adminsettings,notification,addstore])

dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=buf, title='Python Selenium Magento Automation Report', description='Moduels Tested: \n\n 1.Signin \n\n 2.Add Product \n\n 3.Add Customer \n\n 4.Admin Settings \n\n 5.Notification \n\n 6.Add New Store')

runner.run(test_suite)