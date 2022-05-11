import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")
browser.get("http://naver.com")
time.sleep(5)
browser.close()

# browser = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     options=webdriver.ChromeOptions()
# )
# browser.get("http://www.google.com")
# print(browser.title)
# browser.close()