#!/usr/bin/python

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from info import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create browser driver object

driver = webdriver.Edge()

# open the web page

dirver.get("http://47.100.131.240/demo1/index.html")


# set the auto wait time

wait = WebDriverWait(dirver, 20)

element = wait.until(EC.presence_of_element_located(
    By.ID, 'canvas'))

element.screenshot("code.png")

client = Chaojiying(
        chaojiying_username, chaojiying_pwd, chaojiying_softid)


data = open("code.png", "rb").read()

result = client.post_pic(data, "1006")

code = result["pic_str"]
