from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Tworzę obiekt z klasy
przegladarka = webdriver.Chrome()
print(type(przegladarka))
przegladarka.get("http://duckduckgo.com")
przegladarka.save_screenshot("skrin.png")
pole_wyszukiwania = przegladarka.find_element(By.ID, "searchbox_input")
print(type(pole_wyszukiwania))
pole_wyszukiwania.send_keys("Kozminski")
pole_wyszukiwania.submit()
sleep(30)