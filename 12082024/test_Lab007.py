import time
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Verify that URL Changes when we click on the Make appointment button")
@allure.description("Verify the URL changes")



def test_mini_project_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
#    time.sleep(10)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.quit()
