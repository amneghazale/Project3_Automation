from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By


chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
service_obj=Service("../ChromeDriver/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()

#Search painting By write one word
driver.get("http://127.0.0.1:5000/")
driver.find_element(By.ID, "searchBar").send_keys("american")
time.sleep(3)
driver.find_element(By.ID, "submit").click()

time.sleep(3)

# Search painting by writing the first letters
driver.get("http://127.0.0.1:5000/")
driver.find_element(By.ID, "searchBar").send_keys("am")
time.sleep(3)
driver.find_element(By.ID, "submit").click()
time.sleep(3)

# Search painting by writing the full name in small letters
driver.get("http://127.0.0.1:5000/")
driver.find_element(By.ID, "searchBar").send_keys("american gothic")
time.sleep(3)
driver.find_element(By.ID, "submit").click()
time.sleep(3)

# Search painting by writing the full name in capital letters
driver.get("http://127.0.0.1:5000/")
driver.find_element(By.ID, "searchBar").send_keys("AMERICAN GOTHIC")
time.sleep(3)
driver.find_element(By.ID, "submit").click()
time.sleep(3)

# Search painting by writing the name of the painting in small and capital letters
driver.get("http://127.0.0.1:5000/")
driver.find_element(By.ID, "searchBar").send_keys("aMerIcan GOtHic")
time.sleep(3)
driver.find_element(By.ID, "submit").click()





