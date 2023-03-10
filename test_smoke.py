from selenium.webdriver.common.by import By
import time
import pytest
from BaseClass import  BaseClass

@pytest.mark.usefixture("setup")
@pytest.mark.smoke

class TestSmoke(BaseClass):
    def test_title_homepage(self, setup):
        setup.get("http://127.0.0.1:5000/")
        print(setup.find_element(By.TAG_NAME,"h1").text)
        assert setup.find_element(By.TAG_NAME,"h1").text=="Famous Paintings"
        log = self.getLogger()
        log.info("Title is verified and found correct")

    def test_OpenSite(self, setup):
        setup.get("http://127.0.0.1:5000/")
        assert  setup.current_url=="http://127.0.0.1:5000/", "Don't found the site"
        print("Passed")
        log = self.getLogger()
        log.info("The site opened and we reached in the homePage")

    def  test_PageAddPainting(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='../static/image112.png']").click()
        assert setup.current_url=="http://127.0.0.1:5000/add_data", "Not found the page add painting"
        print("Passed")
        log = self.getLogger()
        log.info("The site opened and we reached in the Add paintind page")

    def test_Alter(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.get("http://127.0.0.1:5000/alter_painting/1")
        assert setup.current_url=="http://127.0.0.1:5000/alter_painting/1"
        print("Passed")
        log = self.getLogger()
        log.info("The painting alter")

    def test_current_location(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.CSS_SELECTOR, " img[src='/display/caffe%20terras%20at%20night.jpg']").click()
        print(setup.find_element(By.CSS_SELECTOR, "body > ol:nth-child(2) > p:nth-child(12)").text)
        assert setup.find_element(By.CSS_SELECTOR, "body > ol:nth-child(2) > p:nth-child(12)").text == "1888"
        log = self.getLogger()
        log.info(" Cafe Terrace at Night current location verified ")


def test_crossBrowser(crossBrowser):
        print(crossBrowser)


