from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pandas as pd
import pymysql
import mysql.connector
from sqlalchemy import create_engine

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

flight_data = []

browser = webdriver.Chrome()
url = 'https://flight.naver.com/'
browser.get(url)

time.sleep(1) # 1초 대기
# 편도 버튼 찾아 누르기
one_way = browser.find_element(By.XPATH, '//i[text() = "편도"]')
one_way.click()

time.sleep(1)
start = browser.find_element(By.XPATH, '//button[@class="tabContent_route__1GI8F select_City__2NOOZ start"]')
start.click()

wait_until('//button[text() = "국내"]')
korea = browser.find_element(By.XPATH, '//button[text() = "국내"]')
korea.click()

wait_until('//i[text() = "인천, 김포국제공항"]')
osaka  = browser.find_element(By.XPATH, '//i[contains(text(), "인천, 김포국제공항")]')
osaka.click()

time.sleep(1)
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

wait_until('//button[text() = "일본"]')
japan = browser.find_element(By.XPATH, '//button[text() = "일본"]')
japan.click()

wait_until('//i[text() = "간사이국제공항"]')
osaka  = browser.find_element(By.XPATH, '//i[contains(text(), "간사이국제공항")]')
osaka.click()

time.sleep(1)
begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()


for date_number in range(22, 32):
    xpath_expression = f'//b[text() = "{date_number}"]'

    time.sleep(random.uniform(2,4))
    # wait_until('//b[text() = "1"]')
    day_num = browser.find_elements(By.XPATH, xpath_expression)
    day_num[0].click()

    wait_until('//span[text() = "항공권 검색"]')
    search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
    search.click()

    elem = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '//div[@class = "indivisual_IndivisualItem__3co62 result"]')))
    print(elem.text)

    time.sleep(random.uniform(2,4))
    # 요소들을 가져오기 위해 find_elements 사용
    elements = browser.find_elements(By.XPATH, '//div[@class="indivisual_IndivisualItem__3co62 result"]')

    # 튜플로 저장
    for element in elements:
        month = 7
        day = date_number
        air_class = "일반석"
        airline_name = element.find_element(By.CLASS_NAME, 'name').text
        departure_time = element.find_element(By.CLASS_NAME, 'route_time__-2Z1T').text
        departure_airport = element.find_element(By.CLASS_NAME, 'route_code__3WUFO').text
        arrival_time = element.find_elements(By.CLASS_NAME, 'route_time__-2Z1T')[1].text
        arrival_airport = element.find_elements(By.CLASS_NAME, 'route_code__3WUFO')[1].text
        duration = element.find_element(By.CLASS_NAME, 'route_info__1RhUH').text
        price = element.find_element(By.CLASS_NAME, 'item_num__3R0Vz').text
        flight_data.append((month, day, air_class, airline_name, departure_time, departure_airport, arrival_time, arrival_airport, duration, price))

    time.sleep(random.uniform(2,4))
    # 버튼 요소 찾기
    change = browser.find_element(By.CLASS_NAME, 'tabContent_options__KwvIB')
    # 버튼 클릭
    change.click()

for date_number in range(1, 5):

    xpath_expression = f'//b[text() = "{date_number}"]'

    time.sleep(random.uniform(2,4))
    # wait_until('//b[text() = "1"]')
    day_num = browser.find_elements(By.XPATH, xpath_expression)
    day_num[1].click()

    wait_until('//span[text() = "항공권 검색"]')
    search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
    search.click()

    elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class = "indivisual_IndivisualItem__3co62 result"]')))
    print(elem.text)

    time.sleep(random.uniform(2,4))
    # 요소들을 가져오기 위해 find_elements 사용
    elements = browser.find_elements(By.XPATH, '//div[@class="indivisual_IndivisualItem__3co62 result"]')

    # 튜플로 저장
    for element in elements:
        month = 8
        day = date_number
        air_class = "일반석"
        airline_name = element.find_element(By.CLASS_NAME, 'name').text
        departure_time = element.find_element(By.CLASS_NAME, 'route_time__-2Z1T').text
        departure_airport = element.find_element(By.CLASS_NAME, 'route_code__3WUFO').text
        arrival_time = element.find_elements(By.CLASS_NAME, 'route_time__-2Z1T')[1].text
        arrival_airport = element.find_elements(By.CLASS_NAME, 'route_code__3WUFO')[1].text
        duration = element.find_element(By.CLASS_NAME, 'route_info__1RhUH').text
        price = element.find_element(By.CLASS_NAME, 'item_num__3R0Vz').text
        flight_data.append((month, day, air_class, airline_name, departure_time, departure_airport, arrival_time, arrival_airport, duration, price))

    time.sleep(random.uniform(2,4))
    # 버튼 요소 찾기
    change = browser.find_element(By.CLASS_NAME, 'tabContent_options__KwvIB')
    # 버튼 클릭
    change.click()


df = pd.DataFrame(flight_data, columns=['month', 'day', 'air_class', 'airline_name', 'departure_time', 'departure_airport', 'arrival_time', 'arrival_airport', 'duration', 'price'])
df.to_excel('osaka_data.xlsx')

"""
# MySQL 연결 정보
host = '127.0.0.1:3306'
user = 'root'
password = 'ax1010ax1010'
database = '당신의_mysql_데이터베이스'

# MySQL 서버에 연결합니다
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# SQLAlchemy를 사용하여 'osaka_air' 테이블을 생성합니다
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
df.to_sql('osaka_air', engine, index=False, if_exists='replace')

# MySQL 연결을 닫습니다
connection.close()
"""

input("종료하려면 엔터키 입력하세요")
browser.quit()
