from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():

    chrome_options = Options()
    #chrome_options.add_extension("C:/Users/shruti/Downloads/adBlock.crx")
    chrome_options.add_argument("--page-load-strategy=eager")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")

    # Maximize the browser window
    driver.maximize_window()
    driver.quit()
