from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pyperclip

chrome = webdriver.Chrome("./Users/sabin/Desktop/Learned/web_crawling/dynamic_crawling/myvenv/chromedriver")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("http://shopping.naver.com")

def css_selector(wait,css_selector):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

#login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))) 보이는지와 존재하는지의 차이! 대부분 보이는 것으로 사용 visibility_of_element_located
login_button = css_selector(wait,"a#gnb_login_button")
login_button.click()

time.sleep(1)
input_id = css_selector(wait,"input#id")
input_pw = css_selector(wait,"input#pw")

pyperclip.copy("sabin5105")
input_id.send_keys(Keys.COMMAND, 'v')
pyperclip.copy("d01077112739")
input_pw.send_keys(Keys.COMMAND, 'v')
input_pw.send_keys("\n")

short_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a#gnb_logout_button")))

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
search.send_keys("맥북 케이스")
time.sleep(1)
search.send_keys("\n")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class^=basicList_info_area__]")))

# 무한스크롤
# for i in range(8):
#     chrome.execute_script("window.scrollBy(0, " + str((i+1 * 1000) + ")")
#     time.sleep(1)

# items = chrome.find_elements_by_css_selector("div[class^=basicList_info_area__]")
# for item in items:
#     # 광고 제거
#     try:
#         item.find_element_by_css_selector("button[class^=ad_]")
#         continue
#     except:
#         pass
#     print(item.find_element_by_css_selector("a[class^=basicList_link__]").text)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class^=basicList_link__]"))).click()

time.sleep(2)
chrome.switch_to.window(chrome.window_handles[1])

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[aria-haspopup='listbox']")))
options = chrome.find_elements_by_css_selector("a[aria-haspopup='listbox']")

# 1번 옵션
options[0].click()
time.sleep(0.1)
chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(2) a[role=option]").click()
# 2번 옵션
# options[1].click()
# time.sleep(0.1)
# chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(1) a[role=option]").click()
chrome.find_element_by_css_selector("div[class$=buy] a").click()

time.sleep(3)

