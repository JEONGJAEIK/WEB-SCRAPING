from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import os

browser = webdriver.Chrome('C:/Users/wodlr/chromedriver/chromedriver')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

browser.implicitly_wait(3)
browser.get('https://pp.kepco.co.kr/')

ID = browser.find_element(By.ID, 'RSA_USER_ID')
ID.send_keys('')
PW = browser.find_element(By.ID, 'RSA_USER_PWD')
PW.send_keys('')
Element = browser.find_element(By.CLASS_NAME, 'intro_btn')
Element.click()

browser.get('https://pp.kepco.co.kr/cc/cc0102.do?menu_id=O010402')
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
my_notices = soup.select('body')

data = {}

for notices in my_notices:
    data[notices.text] = notices.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)