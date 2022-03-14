import time

from selenium import webdriver
from time import sleep

import text
import get_price

PATH = "D:\chromedriver\chromedriver"
driver = webdriver.Chrome(PATH)
mail = "se7u4v6g@abv.bg"
pw = "12345678cr"
send_to = ["vasilsonicsiromahov@gmail.com"]


def abv_bg():
    driver.get("https://www.abv.bg/")
    print("\nopening abv.bg")

    sleep(10)
    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/p[1]/input"). \
        send_keys(mail)
    print(mail)
    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/p[2]/input"). \
        send_keys(pw)
    print(pw)

    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/p[3]/input").click()
    print("\nLogin")

    # new message
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[3]/div").click()
    print("\nnew message")

    # to me
    sleep(2)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/input"). \
        send_keys(send_to[0])
    print(f"\nsend to {send_to[0]}")
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td").click()
    sleep(2)

    # title
    sleep(2)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[5]/td[2]/div/input"). \
        send_keys("BOT: CRYPTO ANNOUNCEMENT ")
    print("\nBOT: CRYPTO ANNOUNCEMENT ")

    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/iframe"). \
        send_keys(text.text)
    print("\npaste text")

    sleep(5)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[4]/div/div[4]/div/div[4]/div/div[2]/div/div[2]/div/div[1]/div[1]"). \
        click()
    print("\nsent")
    time.sleep(4)
    driver.quit()


while True:
    abv_bg()
    time.sleep()
