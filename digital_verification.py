#!/usr/bin/python

import time
from selenium import webdirver
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying
from info import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create a browser driver object
driver = webdriver.Edge()

# 打开网页
driver.get("http://47.100.131.240/demo1/index.html")

# 智能等待
wait = WebDriverWait(driver, 20)
# 直到出现验证码图
element = wait.until(EC.presence_of_element_located((By.ID, 'canvas')))

# 截取验证码图,保存的文件名为code.png
element.screenshot("code.png")

# 填写超级鹰的用户名，密码以及在超级鹰上类似密钥的字符串
client = Chaojiying(chaojiying_username, chaojiying_pwd, chaoyijing_softid)


# 获取到图片的数据
data = open("code.png", "rb").read()

# 调用post_pic 向超级鹰的服务端发请求
result = client.post_pic(data, "1006")

# 获取到结果
code = result.["pic_str"]

# 将结果输入到文本框中
dirver.find_element(By.CLASS_NAME, "input-val").send_keys(code)

# 点击提交验证
dirver.find_element(By.CLASS_NAME, "btn").click()


# 不让浏览器关闭
time.sleep(10000)



