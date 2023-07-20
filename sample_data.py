from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

browser = webdriver.Chrome()
url = 'https://flight.naver.com/'
browser.get(url)

begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

time.sleep(1) # 1초 대기
#WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "27"]')))

# wait_until('//b[text() = "27"]')
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day27[0].click()

day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')
day31[0].click()

arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

wait_until('//button[text() = "일본"]')
domestic = browser.find_element(By.XPATH, '//button[text() = "일본"]')
domestic.click()

wait_until('//i[text() = "간사이국제공항"]')
jeju  = browser.find_element(By.XPATH, '//i[contains(text(), "간사이국제공항")]')
jeju.click()

wait_until('//span[text() = "항공권 검색"]')
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class = "concurrent_ConcurrentItemContainer__2lQVG result"]')))
print(elem.text)

input("종료하려면 엔터키 입력하세요")
browser.quit()