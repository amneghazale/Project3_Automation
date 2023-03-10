from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(8)
driver.maximize_window()
driver.get("http://127.0.0.1:5000/")

# Add new painting

driver.find_element(By.XPATH,"//img[@src='../static/image112.png']").click()
driver.find_element(By.NAME,'filename').send_keys("C:/Users/amnes/OneDrive/Desktop/painting.jpg")
driver.find_element(By.NAME,'painting_title').send_keys("The Most Famous Paintings in the World")
driver.find_element(By.NAME,'description').send_keys("Which are your favorite famous art paintings? Are they on our list of the world’s most famous paintings? Perhaps you will discover a few famous artworks you have not heard of before. Let’s dive into our list of the world’s most popular paintings.")
driver.find_element(By.NAME,'artist').send_keys("Sandro Botticelli")
driver.find_element(By.NAME,'current_location').send_keys("Uffizi Gallery")
driver.find_element(By.NAME,'date_created').send_keys("1482")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='button button5']").click()
time.sleep(3)

# Return to added painting

driver.get("http://127.0.0.1:5000/alter_painting/11")
time.sleep(3)
driver.find_element(By.NAME,'painting_title').send_keys("Amne Ghzale")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='button button5']").click()
time.sleep(3)

# Delete the painting

driver.find_element(By.XPATH, "//button[@class='button button4']").click()