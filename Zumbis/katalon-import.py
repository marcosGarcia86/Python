# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCaseLoginEPaginacao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_login_e_paginacao(self):
        driver = self.driver
        driver.get("https://elicitacao.com.br/")
        driver.find_element_by_id("nm_email_usuario").click()
        driver.find_element_by_id("nm_email_usuario").clear()
        driver.find_element_by_id("nm_email_usuario").send_keys("admin@forseti.com.br")
        driver.find_element_by_id("nm_usu_senha").click()
        driver.find_element_by_id("nm_usu_senha").clear()
        driver.find_element_by_id("nm_usu_senha").send_keys("pert0shyx6ve")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div/ul/li[2]/a/span").click()
        time.sleep(10)
        driver.find_element_by_name("nu_licitacao").click()
        driver.find_element_by_name("nu_licitacao").clear()
        driver.find_element_by_name("nu_licitacao").send_keys("12017")
        driver.find_element_by_xpath("//input[@value='Buscar']").click()
        driver.find_element_by_xpath("//table[@id='table-licitacao']/tbody/tr[17]/td[7]").click()
        driver.find_element_by_link_text("Forseti Tecnologia").click()
        driver.find_element_by_link_text("Logout").click()
        driver.close()
        driver.close()
        driver.find_element_by_id("nm_email_usuario").click()
        driver.find_element_by_id("nm_email_usuario").clear()
        driver.find_element_by_id("nm_email_usuario").send_keys("admin")
        driver.find_element_by_id("nm_email_usuario").send_keys(Keys.DOWN)
        driver.find_element_by_id("nm_email_usuario").send_keys(Keys.TAB)
        driver.find_element_by_id("nm_usu_senha").clear()
        driver.find_element_by_id("nm_usu_senha").send_keys("pert0shyx6ve")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//li[2]/div/span").click()
        driver.find_element_by_link_text(u"Buscar Licitação").click()
        driver.find_element_by_name("nu_licitacao").click()
        driver.find_element_by_name("nu_licitacao").clear()
        driver.find_element_by_name("nu_licitacao").send_keys("12017")
        driver.find_element_by_xpath("//input[@value='Buscar']").click()
        driver.find_element_by_xpath("//table[@id='table-licitacao']/tbody/tr[31]/td[4]").click()
        driver.close()
        driver.find_element_by_id("nm_email_usuario").click()
        driver.find_element_by_id("nm_email_usuario").clear()
        driver.find_element_by_id("nm_email_usuario").send_keys("admin@forseti.com.br")
        driver.find_element_by_id("nm_usu_senha").click()
        driver.find_element_by_id("nm_usu_senha").clear()
        driver.find_element_by_id("nm_usu_senha").send_keys("pert0shyx6ve")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div/ul/li[2]/a/span/em").click()
        driver.find_element_by_name("nu_licitacao").click()
        driver.find_element_by_name("nu_licitacao").clear()
        driver.find_element_by_name("nu_licitacao").send_keys("12017")
        driver.find_element_by_xpath("//input[@value='Buscar']").click()
        driver.find_element_by_xpath("//table[@id='table-licitacao']/tbody/tr[30]/td[7]").click()
        driver.find_element_by_xpath("//table[@id='table-licitacao']/tbody/tr[38]/td[7]").click()
        driver.find_element_by_link_text("Pregao_Eletronico_n_01_2017_SERVICO_RADIOLOGIA_DIGITAL_VET_EDITAL.pdf").click()
        driver.find_element_by_link_text("Forseti Tecnologia").click()
        driver.find_element_by_link_text("Logout").click()
        driver.close()
    
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
