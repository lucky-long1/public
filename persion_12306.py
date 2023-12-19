import datetime
import time
import win32com.client
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

def isElementExist(driver):
    flag = True
    ele = driver.find_elements(by=By.CLASS_NAME, value='btn72')
    # print("ele : ", ele)
    # print("len = ", len(ele))
    if len(ele) == 0:
        flag = False
        return flag
    if len(ele) == 1:
        return flag
    else:
        flag = False
        return flag

# 选择edge浏览器并打开
driver = webdriver.Edge()
# 网页地址
driver.get("https://www.12306.cn/index/")


time.sleep(3)
# 点击登录按钮
driver.find_element(By.ID, 'J-btn-login').click()
# 最大化网页窗口
driver.maximize_window()
# 点击扫码登录
driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[2]/a').click()

time.sleep(20)

# 点击车票预定
driver.find_element(By.ID, 'link_for_ticket').click()

time.sleep(3)

# 选择出发地
driver.find_element(By.ID, 'fromStationText').click()
driver.find_element(By.ID, 'fromStationText').clear()
# 输入出发地
driver.find_element(By.ID, 'fromStationText').send_keys("广州南")
time.sleep(1)
# 确认出发地
driver.find_element(By.ID, 'fromStationText').send_keys(Keys.ENTER)

# 选择目的地
driver.find_element(By.ID, 'toStationText').click()
driver.find_element(By.ID, 'toStationText').clear()
# 输入目的地
driver.find_element(By.ID, 'toStationText').send_keys("马踏")
time.sleep(1)
# 确认目的地
driver.find_element(By.ID, 'toStationText').send_keys(Keys.ENTER)
driver.implicitly_wait(5)

# 选择出发日期
driver.find_element(By.ID, 'train_date').click()
driver.find_element(By.ID, 'train_date').clear()
# 输入日期  格式：YYYY-mm-dd 例：2023-10-15
driver.find_element(By.ID, 'train_date').send_keys("2023-12-30")
time.sleep(1)
driver.find_element(By.ID, 'train_date').send_keys(Keys.ENTER)

# 选择乘车人类型
# 如果是学生选择注这行
driver.find_element(By.ID, 'sf1').click()
# 如果不是学生请选择注释这行
# driver.find_element(By.ID, 'sf2').click()

time.sleep(3)

# 获取查询
query_tag = driver.find_element(By.ID, 'query_ticket')
'''
# 获取当前时间戳
start = time.time()


while True:
    driver.implicitly_wait(5)
    # 点击查询
    driver.execute_script("$(arguments[0]).click()", query_tag)
    # 判断页面中有没有“预订”按钮，如果没有预订按钮就不断查询直到车票开售
    if not isElementExist(driver):
        # 车票处于待开售状态
        print(f"10点00分起售，现在是{time.strftime('%H:%M:%S', time.localtime())}，还未开始售票")
        # 每隔两分钟刷新一次，否则3分钟内无购票操作12306系统会自动登出
        if time.time() - start >= 120:
            driver.refresh()
            start = time.time()
        # 延时1秒防止过于快速地点击导致查询超时，当然偶尔还是会出现超时现象，不过超时也没关系，一般等待6秒之后就会继续自动查询
        time.sleep(1)
        continue
'''

# 定义时间以及获取当前时间
times = '2023-12-18 17:14:00'

###### 问题：出现一直点击查询的操作，不会进入获取票的环节
while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    if now > times:
    #     # 持续点击查询，直到开始时间
    #     driver.find_element(By.ID, 'query_ticket').click()
    #     time.sleep(0.1)
    #     continue

    # else:

        # 点击查询
        driver.find_element(By.ID, 'query_ticket').click()

        # 获取所有车票
        tickets = driver.find_elements(By.XPATH, '//*[@id="queryLeftTable"]/tr')
        # 每张车票有两个tr，但是第二个tr没什么用
        tickets = [tickets[i] for i in range(len(tickets) - 1) if i % 2 == 0]
        for ticket in tickets:
            # 输入车次
            if ticket.find_element(By.CLASS_NAME, 'number').text == "C6901" and ticket.find_element(By.XPATH, '//td[8]').text != "候补":
                # 点击预定
                ticket.find_element(By.CLASS_NAME, 'btn72').click()
                # 只购买二等座
                # 选择乘车人，如果是学生，则需要确认购买学生票
                driver.find_element(By.XPATH, '//*[@id="normalPassenger_0"]').click()
                # 点击确认购买学生票，如果不是学生，把这行注释了就行
                # driver.find_element(by=By.XPATH, value='//*[@id="dialog_xsertcj_ok"]').click()
                # 提交订单
                driver.find_element(By.XPATH, '//*[@id="submitOrder_id"]').click()

                # 下面的XPATH选择绝对路径，直接使用id和xpath或class定位不到
                # 选择座位 这里是 F 位 ， 如果想选A,B,C,D就把id=“1F”改为相应的字母即可
                wait = WebDriverWait(driver, 3)
                element = wait.until(ec.presence_of_element_located((
                    By.XPATH, '//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[2]/li[2]/a[@id="1F"]')))
                element.click()

                # try:
                    #  选择座位 A
                    # driver.find_element(By.XPATH, '//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[2]/li[2]/a[@id="1A"]').click()
                    #  选择座位 B
                    # driver.find_element(By.XPATH, '//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[2]/li[2]/a[@id="1B"]').click()
                    #  选择座位 C
                    # driver.find_element(By.XPATH, '//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[2]/li[2]/a[@id="1C"]').click()
                    #  选择座位 D
                    # driver.find_element(By.XPATH, '//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[2]/li[2]/a[@id="1D"]').click()
                    #  选择座位 F
                #     driver.find_element(By.XPATH, '//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[2]/li[2]/a[@id="1F"]').click()
                # except:
                #     pass
                # 跟上面一样需要绝对路径，点击确认座位
                driver.find_element(By.ID, 'qr_submit_id').click()
                # driver.find_element(By.XPATH, '//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[8]/a[2]qr_submit_id').click()
        break

# time.sleep(100000)











