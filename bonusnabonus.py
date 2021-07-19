from selenium import webdriver
import Locators
import Constants
import time

driver=webdriver.Chrome()
driver.get(Constants.BASE_URL)
driver.maximize_window
time.sleep(3)
dugmePrijaviSe = driver.find_element_by_css_selector(Locators.dugmePrijaviSe)
dugmePrijaviSe.click()
email_polje = driver.find_element_by_css_selector(Locators.login_Email)
email_polje.send_keys("mailzanoviprojekat@gmail.com")
lozinka_polje = driver.find_element_by_css_selector(Locators.login_Lozinka)
lozinka_polje.send_keys("Lozinka1234")
time.sleep(3)
loginDugme = driver.find_element_by_css_selector(Locators.login_button)
loginDugme.click()
time.sleep(5)

memeDugme = driver.find_element_by_css_selector(Locators.memeButton)
memeDugme.click()
