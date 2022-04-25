from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") # sandbox
#options.add_argument("headless") # 창 제거

chrome = webdriver.Chrome("./chromedriver",options=options)
chrome.get("http://naver.com")
chrome.get("http://shopping.naver.com")
chrome.back()
chrome.forward()

time.sleep(2)
chrome.close()
