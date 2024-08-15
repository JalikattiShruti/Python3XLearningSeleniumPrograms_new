import time
import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.mark.Negative
@allure.title("VWO Invalid Login Page - test_mini_project_2")
@allure.description("Verify that with Invalid Email, Password. Error message seen")


def test_mini_project_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"

    email_web_element = driver.find_element(By.NAME, "username")
    email_web_element.send_keys("admin@admin.com")

    password_web_element = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password_web_element.send_keys("admin@123")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    time.sleep(4)


    error_message_web_element = driver.find_element(By.ID, "js-notification-box-msg")
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
    driver.quit()











# <button type="submit"
# id="js-login-btn"
# class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
# onclick="login.login(event)"
# data-qa="sibequkica">
# <span class="icon loader hidden"
# data-qa="zuyezasugu">
# </span><span data-qa="ezazsuguuy">
# Sign in</span>
# </button>



# <input
# type="password"
# class="text-input W(100%)"
# name="password"
# id="login-password"
# data-qa="jobodapuxe"
# data-gtm-form-interact-field-id="0">

#    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
#   email_webelement = driver.find_element(By.ID, "login-username")

#Id -> name -> classname -> link/partial -> tagname -> css selector -> xpath.
    #<input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi">
#    make_appointment_element.click()
#    time.sleep(10)

#    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

#    driver.quit()
