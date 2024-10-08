import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.Positive
@allure.title("Open the sign up url of vwo.com - test_mini_project_3")
@allure.description("Verify that clicking on the signup button url changes")


def test_mini_project_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"

#    anchor_tag_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Start a free")
    anchor_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(5)
    driver.quit()
