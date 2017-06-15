#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import time
from flask import Flask, render_template

app = Flask(__name__)

r = requests.get("http://www.toutiao.com/api/pc/focus/")  # 今日头条网站头条新闻的接口
r.encoding = 'utf-8'
data = json.loads(r.text)
_data_list = data["data"]["pc_feed_focus"]     #_data_list为列表形式，每一个元素为一个字典，后面用到了其中的'title'、'image_url'、'display_url'这些key


@app.route('/')     #在浏览器的地址栏中输入127.0.0.1:5000/即可访问到home函数返回的html文件，并在浏览器中展示出来
def home():
    data_list = _data_list[:6]     #取其中的前6条新闻

    r2 = requests.get("http://www.toutiao.com/stream/widget/local_weather/data/?city=")   #获取城市信息
    r2.encoding = 'utf-8'
    data2 = json.loads(r2.text)
    city = data2["data"]["city"]

    local_time = time.localtime(time.time())
    return render_template('home.html', data_list=data_list, city=city, time=local_time)  #使用模版机制，将获取到的信息传入home.html中


@app.route(_data_list[0]['display_url'])
def display0():
    url = "http://www.toutiao.com" + _data_list[0]['display_url'] + "#p=1"  #今日头条中的相应热点新闻的详情链接
    return requests.get(url).text    #获取它的html并展示到自己的页面中


@app.route(_data_list[1]['display_url'])
def display1():
    url = "http://www.toutiao.com" + _data_list[1]['display_url'] + "#p=1"
    return requests.get(url).text


@app.route(_data_list[2]['display_url'])
def display2():
    url = "http://www.toutiao.com" + _data_list[2]['display_url'] + "#p=1"
    return requests.get(url).text


@app.route(_data_list[3]['display_url'])
def display3():
    url = "http://www.toutiao.com" + _data_list[3]['display_url'] + "#p=1"
    return requests.get(url).text


@app.route(_data_list[4]['display_url'])
def display4():
    url = "http://www.toutiao.com" + _data_list[4]['display_url'] + "#p=1"
    return requests.get(url).text


@app.route(_data_list[5]['display_url'])
def display5():
    url = "http://www.toutiao.com" + _data_list[5]['display_url'] + "#p=1"
    return requests.get(url).text


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

