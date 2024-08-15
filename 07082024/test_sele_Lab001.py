from selenium import webdriver


def test_sample():
    driver = webdriver.Edge()
    driver.get("https://www.youtube.com")
    assert driver.current_url == "https://www.youtube.com"


