#!/usr/bin/python

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriveer.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

word = input("please enter what you translation words: ")

# 创建一个浏览器的驱动对象
driver = webdriver.Edge()

# 打开百度翻译的网站
driver.get("https://fanyi.baidu.com")

# 找到关闭按钮，并点击
close_btn = driver.find_element(By.CLASS_NAME, 'desktop-guige-close')

close_btn.click()

# 找到文本框
input_box = driver.find_element(By.ID, 'baidu_translate_input')
input_box.send_keys(word)

# 找到“立即翻译”按钮，并点击
translate_btn = driver.find_element(By.ID, 'translate-button')
translate_btn.click()

time.sleep(5)

# 获取结果,方法一：如果翻译时间过长，不会等待，可能会出错，或值为空
ele = driver.find_element(By.CLASS_NAME, 'target-output')
result = ele.text

# 获取结果，方法二：智能等待翻译结果
ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'target-output')))

result = ele.text

print(result)


# 让浏览器不关闭
time.sleep(10000)
