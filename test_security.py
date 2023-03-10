from selenium.webdriver.common.by import By
import time
import pytest
from BaseClass import  BaseClass

@pytest.mark.usefixture("setup")
@pytest.mark.security

class TestSecurity(BaseClass):

    def test_AddReView(self, setup):
        setup.get("http://127.0.0.1:5000/painting_info/8")
        befor_AddReview=setup.find_elements(By.XPATH, "//body//ol//br")
        # provide only name for review
        setup.find_element(By.NAME, "name").send_keys("Amne")
        setup.find_element(By.XPATH, "//button[@class='button button5']").click()
        after_AddReview = setup.find_elements(By.XPATH, "//body//ol//br")
        assert len(befor_AddReview) < len(after_AddReview), "faild to add review due to missing mandatory attribute "
        print(" The review has been added")
        log = self.getLogger()
        log.info("The review has been added")

    def test_AddSamePainting(self, setup):
        setup.get("http://127.0.0.1:5000/")
        befor_Add = setup.find_elements(By.XPATH, "//div/a")
        setup.find_element(By.XPATH, "//img[@src='../static/image112.png']").click()
        setup.find_element(By.NAME, 'filename').send_keys("C:/Users/amnes/OneDrive/Desktop/MonaLisa.jpg")
        setup.find_element(By.NAME, 'painting_title').send_keys("The Most Famous Paintings in the World")
        setup.find_element(By.NAME, 'description').send_keys("Which are your favorite famous art paintings? Are they on our list of the world’s most famous paintings? Perhaps you will discover a few famous artworks you have not heard of before. Let’s dive into our list of the world’s most popular paintings.")
        setup.find_element(By.NAME, 'artist').send_keys("Sandro Botticelli")
        setup.find_element(By.NAME, 'current_location').send_keys("Uffizi Gallery")
        setup.find_element(By.NAME, 'date_created').send_keys("1482")
        setup.find_element(By.XPATH, "//button[@class='button button5']").click()
        after_Add = setup.find_elements(By.XPATH, "//div/a")
        assert len(after_Add) > len(befor_Add), "faild to Add the painting"
        print("the painting has been added")
        log = self.getLogger()
        log.info("The painting has been added")

    def test_Delete(self, setup):
        setup.get("http://127.0.0.1:5000")
        befor_delete=setup.find_elements(By.XPATH, "//div/a")
        print(len(befor_delete))
        setup.get("http://127.0.0.1:5000/painting_info/11")
        setup.find_element(By.XPATH, "//button[@class='button button4']").click()
        after_delete=setup.find_elements(By.XPATH, "//div/a")
        print(len(after_delete))
        assert len(after_delete) < len(befor_delete), "The painting is not delete"
        log = self.getLogger()
        log.info("The painting was deleted successfully")

    def test_AddRandomPhoto(self, setup):
        setup.get("http://127.0.0.1:5000/")
        befor_delete = setup.find_elements(By.XPATH, "//div/a")
        setup.find_element(By.XPATH, "//img[@src='../static/image112.png']").click()
        setup.find_element(By.NAME, 'filename').send_keys("C:/Users/amnes/OneDrive/Desktop/photo.jpg")
        setup.find_element(By.NAME, 'painting_title').send_keys("The Most Famous Paintings in the World")
        setup.find_element(By.NAME, 'description').send_keys(
            "Which are your favorite famous art paintings? Are they on our list of the world’s most famous paintings? Perhaps you will discover a few famous artworks you have not heard of before. Let’s dive into our list of the world’s most popular paintings.")
        setup.find_element(By.NAME, 'artist').send_keys("Sandro Botticelli")
        setup.find_element(By.NAME, 'current_location').send_keys("Uffizi Gallery")
        setup.find_element(By.NAME, 'date_created').send_keys("1482")
        setup.find_element(By.XPATH, "//button[@class='button button5']").click()
        after_delete = setup.find_elements(By.XPATH, "//div/a")
        assert len(after_delete) > len(befor_delete), "faild to Add the painting"
        print("the painting has been added")
        log = self.getLogger()
        log.info("The painting has been added")


def test_crossBrowser(crossBrowser):
        print(crossBrowser)



