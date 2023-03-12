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

# Open page of random painting

time.sleep(3)
driver.get("http://127.0.0.1:5000/painting_info/3")
time.sleep(3)

# Return to homepage

driver.find_element(By.XPATH, "//img[@src='../static/logo3.jpg']").click()
assert driver.current_url=="http://127.0.0.1:5000/", "FAIL: Clicking home logo did not take to homepage"
print("PASS: Clicking on home logo take to homepage")
