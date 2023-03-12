from selenium.webdriver.common.by import By
import time
import pytest
from BaseClass import  BaseClass

@pytest.mark.usefixture("setup")
@pytest.mark.functional

class TestFunctional(BaseClass):

    def test_RunSearch(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.ID, "searchBar").send_keys("American ")
        setup.find_element(By.ID, "submit").click()
        assert setup.current_url=="http://127.0.0.1:5000/painting_info/10", "found the painting"
        print("Error message")
        log = self.getLogger()
        log.error("painting not found")

    def test_ReviewPainting(self, setup):
        setup.get("http://127.0.0.1:5000/painting_info/11")
        befor_AddReview = setup.find_elements(By.XPATH, "//body//ol//br")
        setup.find_element(By.NAME, "review_text").send_keys("its good")
        setup.find_element(By.XPATH, "//button[@class='button button5']").click()
        after_AddReview = setup.find_elements(By.XPATH, "//body//ol//br")
        assert len(befor_AddReview) < len(after_AddReview), "faild to add due to missing mandatory attribute "
        print("Failed to add review due to missing mandotry attribute")
        log = self.getLogger()
        log.debug("Failed to add review due to missing mandotry attribute")


    def test_AddPainting(self, setup):
        # Add painting without date created:
        setup.get("http://127.0.0.1:5000/")
        befor_Add = setup.find_elements(By.XPATH, "//div/a")
        setup.find_element(By.XPATH, "//img[@src='../static/image112.png']").click()
        setup.find_element(By.NAME, 'filename').send_keys("C:/Users/amnes/OneDrive/Desktop/painting.jpg")
        setup.find_element(By.NAME, 'painting_title').send_keys("The Most Famous Paintings in the World")
        setup.find_element(By.NAME, 'description').send_keys("Which are your favorite famous art paintings? Are they on our list of the world’s most famous paintings? Perhaps you will discover a few famous artworks you have not heard of before. Let’s dive into our list of the world’s most popular paintings.")
        setup.find_element(By.NAME, 'artist').send_keys("Sandro Botticelli")
        setup.find_element(By.NAME, 'current_location').send_keys("Uffizi Gallery")
        # driver.find_element(By.NAME,'date_created').send_keys("1482")
        setup.find_element(By.XPATH, "//button[@class='button button5']").click()
        after_Add = setup.find_elements(By.XPATH, "//div/a")
        assert len(after_Add) > len(befor_Add), "fiald to add painting"
        print("Failed to add painting due to missing mandotry attribute")
        log = self.getLogger()
        log.debug("Failed to add review due to missing mandotry attribute")


    def test_AddReView(self, setup):
        setup.get("http://127.0.0.1:5000/painting_info/9")
        befor_AddReview = setup.find_elements(By.XPATH, "//body//ol//br")
        # provide only name for review
        setup.find_element(By.NAME, "name").send_keys("Amne")
        setup.find_element(By.XPATH, "//button[@class='button button5']").click()
        after_AddReview = setup.find_elements(By.XPATH, "//body//ol//br")
        assert len(befor_AddReview) < len(after_AddReview), "faild to add due to missing mandatory attribute "
        print(" The review has been added")
        log = self.getLogger()
        log.info("The review has been added")

    def test_Search(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.ID, "searchBar").send_keys("Am ")
        setup.find_element(By.ID, "submit").click()
        assert setup.current_url=="http://127.0.0.1:5000/painting_info/10", "found the painting"
        print("Error message")
        log = self.getLogger()
        log.error("painting not found")


