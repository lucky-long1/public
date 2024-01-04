import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying
from info import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
from selenium


# create a browser driver object
driver = webdriver.Edge()

# 获取位置

def get_pos():
    # 通过OpenCV技术标出这个点
    # 读取图片
    image = cv2.imread("code2.png")

    # 获取超级鹰对象
    client = Chaojiying(chaojiying_username, chaojiying_pwd, chaojiying_slidt)

    # 获取到图片数据
    data = open("code2.png", "rb").read()
    result = client.post_pic(data, "9101")
    pos = tuple([int(i) for i in result["pic_str"].split(",")])
    print(pos)
    return pos   # 返回就是坐标

# 打开网页
driver.get("http://47.100.131.240/demo2/index.html")

# 智能等待20秒,直到出现图片
wait = WebDriverWait(driver, 20)
element = wait.until(EC.presence_of_element_located((By.ID, "imgbox")))


time.sleep(3)

# 获取验证码的图片
element.screenshot("code2.png")


while True:
    pos = get_pos()

    # 找到滑块
    btn = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'slider-btn')))

    # 如果要对网页进行一些微复杂的操作，拖拽，滚动等
    # 用户和浏览器进行交互
    action = ActionChains(driver)

    # click_and_hold 鼠标做按住不放动作
    # 按下鼠标左键并保持不放的操作
    action.click_and_hold(btn).perform()

    action.move_to_element_with_offset(btn, pos[0]-30, 0).perform()

    # 释放鼠标左键的操作
    action.release(btn).perform

    msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ver-tips")))

    if msg.text.strip() == "验证通过":
        break


    time.sleep(10000)


