# import time
import time

from selenium import webdriver


def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.refresh()
    driver.back()
    driver.forward()
    print(driver.page_source)
    #    driver.close()
    driver.quit()
    time.sleep(10)

#    driver.maximize_window()
#    time.sleep(10)
