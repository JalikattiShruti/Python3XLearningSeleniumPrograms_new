import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.Positive
@allure.title("Check user validity expiration and prompt for upgrade - test_mini_project_3")
@allure.description("Verify whether the user's validity has expired and if an upgrade is needed.")
def test_mini_project_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    assert driver.current_url == "https://www.idrive360.com/enterprise/login"

    email_web_element = driver.find_element(By.NAME, "username")
    email_web_element.send_keys("augtest_040823@idrive.com")

    password_web_element = driver.find_element(By.ID, "password")
    password_web_element.send_keys("123456")

    sign_in_btn_web_element = driver.find_element(By.ID, "frm-btn")
    sign_in_btn_web_element.click()

    time.sleep(20)

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot')
    upgrade_now = driver.find_element(By.ID, "upgrade")
    upgrade_now.click()
    time.sleep(10)

    upgrade_now = driver.find_element(By.CLASS_NAME, "id-card-title")
    assert upgrade_now.is_displayed()
    allure.attach(driver.get_screenshot_as_png(), name='upgrade_Screenshot')



