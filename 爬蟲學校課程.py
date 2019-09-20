# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:05:32 2019

@author: User
"""

from bs4 import BeautifulSoup
import getpass
import re
import getpass
import requests
s = requests.Session()
url = 'https://ilearn2.fcu.edu.tw/login/index.php'#開f12看清楚
username = input("請輸入學號")
password = getpass.getpass("請輸入密碼")
login = s.get(url)#將網頁資料GET下來
soup= BeautifulSoup(login.text, "html.parser")#將網頁資料>html.parser
value =soup.find_all('input',{"name":"logintoken"})[0]['value']#提取值，記得+上[0]
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}#可不用
data={
    'username':username,
    'password':password,
    'logintoken':value,   
}
page = s.post(url, headers=header, data=data)
bs_class = BeautifulSoup(page.text, 'html.parser')
courseBox = bs_class.find_all("div",class_='coc-mycurricular coursebox clearfix')

for course in courseBox:
    try:
        courseName = course.find_all('div')[0].find('a').text
        teacher = course.find_all('div')[1].find('span').text
        print(courseName+teacher)
    except:
        print(courseName)


