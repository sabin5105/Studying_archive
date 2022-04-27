from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pyperclip

chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("http://shopping.naver.com")

def css_selector(wait,css_selector):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

#login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))) 보이는지와 존재하는지의 차이! 대부분 보이는 것으로 사용 visibility_of_element_located
login_button = css_selector(wait,"a#gnb_login_button")
login_button.click()

input_id = css_selector(wait,"input#id")
input_pw = css_selector(wait,"input#pw")

pyperclip.copy("sabin5105")
input_id.send_keys(Keys.COMMAND, 'v')
pyperclip.copy("d01077112739")
input_pw.send_keys(Keys.COMMAND, 'v')
input_pw.send_keys("\n")

short_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a#gnb_logout_button")))


time.sleep(3)

chrome.close()