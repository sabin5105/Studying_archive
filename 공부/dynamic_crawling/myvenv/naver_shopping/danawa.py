from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome,10)
#main url
url = "https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_gnb_esti"

def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))

def finds_present(css):
    find_present(css)
    return chrome.find_elements_by_css_selector(css)

def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements_by_css_selector(css)

# mapping_table
category ={
    "cpu" : "873",
    "cooler" : "887",
    "mainboard" : "875",
    "memory" : "874",
    "graphiccard" : "876",
    "ssd" : "32617",
    "harddisk" : "877",
    "hdd" : "10620",
    "case" : "879",
    "power" : "880",
    "keyboard" : "881",
    "mouse" : "902",
    "monitor" : "13735",
    "odd" : "878",
    "software" : "901"
}

category_css ={
    c: "dl.pd_list "+"dd.category_" + category[c] + " a" for c in category
}

chrome.get(url)
#find.visible("iframe#ifrmwWish")
#chrome.switch_to.frame("ifrmWish")
# mainboard = find_visible("dl.pd_list "+"dd.category_" + category["cpu"] + " a")
# mainboard.click()

# cpu 카테고리 클릭
find_visible(category_css["cpu"]).click()
time.sleep(1)

# cpu 제조사 불러오기
options = finds_visible("ul.search_cate_list span.item_text")
print("CPU 제조사를 선택하세요")
print(f"1. {options[0].text}")
print(f"2. {options[1].text}")
i = int(input(">>>  "))

options[i-1].click()
time.sleep(5)


chrome.quit()