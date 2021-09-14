from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep


def starting_part():

    browser = webdriver.Chrome(executable_path="/home/ai/Downloads/chrome/chromedriver")
    browser.maximize_window()
    browser.get('https://kite.zerodha.com/')

    user = browser.find_element_by_id("userid")
    password = browser.find_element_by_id("password")

    user.send_keys("")
    password.send_keys("")
    button = browser.find_element_by_class_name("actions")
    button.click()

    sleep(4)

    pin = browser.find_element_by_id("pin")
    pin.send_keys("")
    button = browser.find_element_by_class_name("actions")
    button.click()

    sleep(4)

    order = browser.find_element_by_class_name("orders-nav-item")
    order.click()

    sleep(4)

    download_csv = browser.find_element_by_class_name("download")
    download_csv.click()

    sleep(10)
    browser.quit()