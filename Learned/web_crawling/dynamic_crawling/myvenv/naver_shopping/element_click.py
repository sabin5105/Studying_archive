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
chrome.get("http://shopping.naver.com")
wait = WebDriverWait(chrome,10)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait,"input[name=query]")
search.send_keys("아이폰 케이스\n")

time.sleep(3)

# button = find(wait, "a.co_srh_btn")
# button.click()

# time.sleep(3)

chrome.close()
