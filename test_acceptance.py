from selenium.webdriver.common.by import By
import time
import pytest
from BaseClass import  BaseClass

@pytest.mark.usefixture("setup")
@pytest.mark.acceptance

class TestAcceptance(BaseClass):

    def test_RunSearch(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.ID, "searchBar").send_keys("aMerIcan GOtHic")
        setup.find_element(By.ID, "submit").click()
        print(setup.find_element(By.CSS_SELECTOR, "body > ol:nth-child(2) > p:nth-child(2)").text)
        assert setup.find_element(By.CSS_SELECTOR, "body > ol:nth-child(2) > p:nth-child(2)").text == "American Gothic"
        log = self.getLogger()
        log.info("painting found")


    def test_homepage(self, setup):
        setup.get("http://127.0.0.1:5000/")
    # Open page of random painting
        setup.get("http://127.0.0.1:5000/painting_info/3")
    # Return to homepage
        setup.find_element(By.XPATH, "//img[@src='../static/logo3.jpg']").click()
        assert setup.current_url=="http://127.0.0.1:5000/", "FAIL: Clicking home logo did not take to homepage"
        print("PASS: Clicking on home logo take to homepage")
        log = self.getLogger()
        log.info("Homepage is woking")



    def test_addNewPainiting(self, setup):
        setup.get("http://127.0.0.1:5000/")
        befor_Add = setup.find_elements(By.XPATH, "//div/a")
# Add new painting
        setup.find_element(By.XPATH,"//img[@src='../static/image112.png']").click()
        setup.find_element(By.NAME,'filename').send_keys("C:/Users/amnes/OneDrive/Desktop/painting.jpg")
        setup.find_element(By.NAME,'painting_title').send_keys("The Most Famous Paintings in the World")
        setup.find_element(By.NAME,'description').send_keys("Which are your favorite famous art paintings? Are they on our list of the world’s most famous paintings? Perhaps you will discover a few famous artworks you have not heard of before. Let’s dive into our list of the world’s most popular paintings.")
        setup.find_element(By.NAME,'artist').send_keys("Sandro Botticelli")
        setup.find_element(By.NAME,'current_location').send_keys("Uffizi Gallery")
        setup.find_element(By.NAME,'date_created').send_keys("1482")
        setup.find_element(By.XPATH,"//button[@class='button button5']").click()
        after_Add = setup.find_elements(By.XPATH, "//div/a")
        assert len(after_Add) > len(befor_Add), "fiald to add painting"
        print("New Painting Added")
        log = self.getLogger()
        log.info("The painting has been added")

    def test_AddReview(self, setup):
        setup.get("http://127.0.0.1:5000/painting_info/8")
        setup.find_element(By.NAME, "name").send_keys("Amne")
        setup.find_element(By.NAME, "review_text").send_keys("its good")
        setup.find_element(By.NAME, "rating").send_keys("4")
        setup.find_element(By.XPATH, "//button[@class='button button5']").click()
        assert setup.find_element(By.XPATH, "//button[@class='button button5']").is_displayed(), "The click not display"
        print("Review Added")
        log = self.getLogger()
        log.info("The review has been added")

    def test_alterPainting(self, setup):
        setup.get("http://127.0.0.1:5000/")
        # Add new painting
        setup.find_element(By.XPATH,"//img[@src='../static/image112.png']").click()
        setup.find_element(By.NAME,'filename').send_keys("C:/Users/amnes/OneDrive/Desktop/painting.jpg")
        setup.find_element(By.NAME,'painting_title').send_keys("The Most Famous Paintings in the World")
        setup.find_element(By.NAME,'description').send_keys("Which are your favorite famous art paintings? Are they on our list of the world’s most famous paintings? Perhaps you will discover a few famous artworks you have not heard of before. Let’s dive into our list of the world’s most popular paintings.")
        setup.find_element(By.NAME,'artist').send_keys("Sandro Botticelli")
        setup.find_element(By.NAME,'current_location').send_keys("Uffizi Gallery")
        setup.find_element(By.NAME,'date_created').send_keys("1482")
        setup.find_element(By.XPATH,"//button[@class='button button5']").click()
        # Return to added painting
        setup.get("http://127.0.0.1:5000/alter_painting/11")
        setup.find_element(By.NAME,'painting_title').send_keys("Amne Ghzale")
        setup.find_element(By.XPATH, "//button[@class='button button5']").click()
        assert setup.find_element(By.XPATH, "//p[normalize-space()='Amne Ghzale']").text=="Amne Ghzale", "The click not display"
        print("painting's title has altered")
        log = self.getLogger()
        log.info("painting's title has altered")


def test_crossBrowser(crossBrowser):
        print(crossBrowser)




