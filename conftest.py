from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service_obj = Service("chromedriver_linux64/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(8)
    driver.maximize_window()
    return driver

@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def crossBrowser(request):
    return request.param
