# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):

        login = 'KonDob413'
        password = 'somepassword'
        url = 'redmine.org'
        self.driver = webdriver.Chrome('/usr/local/lib/node_modules/webdriver-manager/selenium/chromedriver_2.41')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_untitled_test_case(self):
        driver = self.driver

        self.open_home_page(driver)

        self.login(driver)

        self.logout(driver)



    def login(self, driver):
        driver.find_element_by_class_name('login').click()
        driver.find_element_by_id('username').send_keys('KonDob413')
        driver.find_element_by_id('password').send_keys('somepassword')
        driver.find_element_by_name('login').click()


    def logout (self, driver):

        driver.find_element_by_class_name('logout').click()




    def open_home_page(self, driver):

        driver.get("https://redmine.org")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
