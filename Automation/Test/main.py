from selenium import webdriver
import time
import unittest
from Automation.Pages.WFHreport import LeavePage
from Automation.Pages.WFHapply import ApplyWFH
from Automation.Pages.login import LoginPAge

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/ankit/PycharmProjects/Atlas/Drivers/chromedriver.exe")
        cls.driver.maximize_window()



    def test_send_wfh(self):

        driver = self.driver

        driver.get("https://vyaguta.lftechnology.com/")
        
        signin = LoginPAge(driver)

        signin.click_continue()
        signin.enter_email("ankitbarwal@lftechnology.com")
        time.sleep(5)
        signin.enter_password('')

        wfhReport = LeavePage(driver)
        wfhReport.click_leave()
        wfhReport.click_wfh()

        wfhReport.copy()
        time.sleep(3)
        wfhReport.send_report()
        time.sleep(3)

        wfhApply = ApplyWFH(driver)
        wfhApply.click_wfh()
        time.sleep(2)
        wfhApply.enter_availability("9-6")
        wfhApply.enter_todo("1. Regression Test on portal and mobile  \n2. Report bug to respective developers")
        time.sleep(3)
        wfhApply.click_emoji()
        time.sleep(2)
        wfhApply.click_apply()
        time.sleep(3)







    @classmethod
    def tearDownClass(cls):
        cls.driver.close()





