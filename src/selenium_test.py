# !/usr/bin/python
# -*- coding: utf-8 -*-

# 宣言部分
import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# chromedriverの設定
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)

# 特定のサイト（Yahoo!検索）にアクセスする
#driver.get("https://www.yahoo.co.jp")
driver.get("https://www.google.com")

# 確認01
#assert 'Yahoo' in driver.title

# 検索窓を操作する
#input_elem = driver.find_element_by_name('p')
#input_elem.clear()
#input_elem.send_keys('Python')
#input_elem.send_keys(Keys.RETURN)

search = driver.find_element_by_name("q")
search.send_keys("Python")
search.submit()




time.sleep(1)
# 確認02
#assert 'Python' in driver.title

# 必要な情報を取得、出力
#for a in driver.find_element_by_class_name('sw-CardBase'):
#    print(a.text)

soup = BeautifulSoup(driver.page_source, "html.parser")
results = soup.find_all("h3", attrs = {"class":"LC20lb"})
for i, result in enumerate(results):
    print("%d : %s" % ( i + 1, result.get_text()))
# 終了処理
driver.close()
