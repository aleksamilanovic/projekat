from selenium import webdriver
import Constants
import Locators
import time


driver=webdriver.Chrome()
driver.get(f"{Constants.BASE_URL}")
dugmePrijaviSe = driver.find_element_by_css_selector(Locators.dugmePrijaviSe)
dugmePrijaviSe.click()
RegistracionoDugme = driver.find_element_by_css_selector(Locators.RegistrujteSE)
RegistracionoDugme.click()
driver.maximize_window

registracijaKI = driver.find_element_by_css_selector(Locators.register_KorisnickoIme)
registracijaEMAIL = driver.find_element_by_css_selector(Locators.register_Email)
registracijaLOZINKA = driver.find_element_by_css_selector(Locators.register_Sifra)
registracijaPL = driver.find_element_by_css_selector(Locators.register_PotvrdaLozinke)

registracijaKI.send_keys("NalogZaProjekat123")
registracijaEMAIL.send_keys("mailzaprojekat123@gmail.com")
registracijaLOZINKA.send_keys("Lozinka12345")
registracijaPL.send_keys("Lozinka12345")

dugmeZaRegistraciju = driver.find_element_by_css_selector(Locators.register_button)
dugmeZaRegistraciju.click()
time.sleep(3)





