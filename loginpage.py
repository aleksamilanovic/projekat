from selenium import webdriver
import Constants
import Locators
import loginPodaci
import time


def TestLogin(username, password):
    driver=webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    prijaviSe = driver.find_element_by_css_selector(Locators.dugmePrijaviSe)
    prijaviSe.click()

    usernameField = driver.find_element_by_css_selector(Locators.login_Email)
    passwordField = driver.find_element_by_css_selector(Locators.login_Lozinka)
    loginButton = driver.find_element_by_css_selector(Locators.login_button)

    usernameField.send_keys(username)
    passwordField.send_keys(password)
    loginButton.click()

    if (driver.current_url==f"{Constants.BASE_URL}{Constants.LOGIN_URL}"):
        print("Niste se ulogovali.")

    else:
        print("Ulogovali ste se.")

    time.sleep(3)
  
    
    


for podatak in loginPodaci.Podaci:
    TestLogin(podatak["username"], podatak["password"])