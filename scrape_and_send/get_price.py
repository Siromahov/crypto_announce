from selenium import webdriver
from math import ceil
from time import sleep

PATH = "D:\chromedriver\chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.tradingview.com/markets/cryptocurrencies/prices-all/")

HOT_price = float(driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div[3]/div[2]/div[4]/table/tbody/tr[92]/td[4]/span").text)
rounded_HOT = ceil(HOT_price * 10000) / 10000
HOT_percentage = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div[3]/div[2]/div[4]/table/tbody/tr[92]/td[8]").text

LTC_price = float(driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div[3]/div[2]/div[4]/table/tbody/tr[21]/td[4]/span").text)
rounded_LTC = ceil(LTC_price * 100) / 100
LTC_percentage = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div[3]/div[2]/div[4]/table/tbody/tr[21]/td[8]").text

BTC_price = float(driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div[3]/div[2]/div[4]/table/tbody/tr[1]/td[4]/span").text)
rounded_BTC = ceil(BTC_price * 100) / 100
BTC_percentage = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div[3]/div[2]/div[4]/table/tbody/tr[1]/td[8]").text

ETH_price = float(driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div/div/div[3]/div[2]/div[4]/table/tbody/tr[2]/td[4]/span").text)
rounded_ETH = ceil(ETH_price * 100) / 100
ETH_percentage = driver.find_element_by_xpath(
"/html/body/div[2]/div[4]/div[2]/div/div/div[3]/div[2]/div[4]/table/tbody/tr[2]/td[8]").text

sleep(2)
driver.quit()
