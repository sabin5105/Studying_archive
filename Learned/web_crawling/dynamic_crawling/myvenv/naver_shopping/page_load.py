from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") # sandbox
#options.add_argument("headless") # 창 제거

chrome = webdriver.Chrome("./chromedriver",options=options)
chrome.get("http://naver.com")
chrome.get("http://shopping.naver.com")
WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
chrome.close()
