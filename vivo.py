# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Vivo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_vivo(self):
        driver = self.driver
        driver.get("http://www.vivo.com.br/portalweb/appmanager/env/web#")
        driver.find_element_by_id("cpfOuEmail").clear()
        driver.find_element_by_id("cpfOuEmail").send_keys("34046044829")
        driver.find_element_by_id("senhaHeader").clear()
        driver.find_element_by_id("senhaHeader").send_keys("260186")
        driver.find_element_by_id("btnEntrar").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("(//a[contains(text(),'x')])[4]").click()
        driver.find_element_by_id("icon_download_0580883543-0").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element_by_xpath("//div[@id='viewer']/div/div[2]/div[98]").click()
        driver.find_element_by_xpath("//div[@id='viewer']/div/div[2]/div[99]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
