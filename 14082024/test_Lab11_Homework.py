import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.Positive
@allure.title("Verify appointment booking process and URL redirection after login - test_mini_project_4")
@allure.description("Test to click the 'Make Appointment' button, verify URL changes, enter credentials, and confirm the final page and URL after successful login.")


def test_mini_project_4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
#    time.sleep(10)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)

    username_web_element = driver.find_element(By.NAME, "username")
    username_web_element.send_keys("John Doe")

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("ThisIsNotAPassword")

    log_in_btn_web_element = driver.find_element(By.ID, "btn-login")
    log_in_btn_web_element.click()
    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(10)

    appointment_text_element = driver.find_element(By.XPATH, "//*[contains(text(),'Make Appointment')]")
    assert appointment_text_element.text == "Make Appointment"

    allure.attach(driver.get_screenshot_as_png(), name='appointment_Screenshot')
    time.sleep(10)
    driver.quit()








