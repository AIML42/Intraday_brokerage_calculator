from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep


def minor_mistake(s):
    total = ''
    for i in s:
        if i == '/':
            break
        else:
            total = total + i

    return total


def brokerage_calulator(stocks_list):

    total_brokerage = 0

    browser = webdriver.Chrome(executable_path="/home/ai/Downloads/chrome/chromedriver")
    # browser.maximize_window()
    browser.get('https://zerodha.com/brokerage-calculator/#tab-equities')

    # equity = browser.find_element_by_class_name("intra intra_bp")
    equity = browser.find_element_by_id("intraday-equity-calc")

    for i in stocks_list:
        buy = int(i[1])
        sell = int(i[2])
        volume = int(minor_mistake(i[3]))

        buy_tab = equity.find_element_by_xpath('//*[@title="Buy Price"]')
        buy_tab.clear()
        buy_tab.send_keys(buy)

        sell_tab = equity.find_element_by_xpath('//*[@title="Sell Price"]')
        sell_tab.clear()
        sell_tab.send_keys(sell)

        vol_tab = equity.find_element_by_xpath('//*[@title="Quantity"]')
        vol_tab.clear()
        vol_tab.send_keys(volume)

        sleep(1)

        brokerage = equity.find_element_by_xpath('//*[@id="intra_total"]')
        total_brokerage += float(brokerage.text)
        print(i, " : ", brokerage.text)

    browser.quit()

    print("Total Brokerage ============> ", total_brokerage)


