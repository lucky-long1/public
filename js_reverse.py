#!/usr/bin/python

import requests
import execjs        #在python里面执行js代码
import time

if __name__ == "__main__":
    with open("demo.js", "r") as f:
        js_code = f.read()

    # 将js字符串变成可以在python里面执行的代码
    ctx = execjs.compile(js_code)

    word = input("please enter translate content: ")
    sign = ctx.call("result: ", word)

    # 获取当前的时间戳，毫秒为单位
    ts = str(int(time.time() * 1000))

    headers = {
    'Origin': 'http://fiddle.jshell.net',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'http://fiddle.jshell.net/_display/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

    data = {
    'msg1': 'wow',
    'msg2': 'such',
    'msg3': 'data',
}

    response = requests.post('http://fiddle.jshell.net/echo/html/', headers=headers, data=data)


    print(response.json()["trans_result"]["data"][0]["dst"])

