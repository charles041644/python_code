# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:10:29 2019

@author: User
"""

from bs4 import BeautifulSoup
import requests,re,os,urllib.request
from urllib.request import urlretrieve
def picture(url,name):
    page3 = requests.get(url,headers = header)
    web3 =BeautifulSoup(page3.text,"html.parser")#解析器
    for i ,n in zip(web3.select('.GalleryImage_image_3lGzO5'),range(100)):
        opener = urllib.request.build_opener()
        opener.addheaders = [('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')]
        urllib.request.install_opener(opener)
        urlretrieve(i.get('src'),os.path.join('D:/abc/dcard',str(name)+str(n)+'.jpg'))
        print(str(name)+str(n))
def tow(url,count):
    a = ''
    header = {
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    page2 = requests.get(url,headers = header)
    web2 =BeautifulSoup(page2.text,"html.parser")#解析器
    
    F=open(str(a)+'txt','w',1,'utf-8')
    for p in web2.select('h2'):#文章title
        file_name = p.text
        F.write(p.text)#寫入標題到資料夾
        F.write('\n')
    for j in web2.select('.Post_content_NKEl9d > div'):#進入每一層
         for k in j.select('div > div'):#找文字 放在 第二層div
            print(k.text)
            F.write(k.text)
            F.write('\n')
    F.close()
    
    new_name = re.split(r'[\\/]',file_name)#正則找名字
    
    a = ('').join(new_name)
#    print('a = {0}'.format(a))
    picture(url,a)

 
if __name__ == '__main__':
    os.chdir('D:/abc')
    try:
         os.mkdir('dcard')#建立FILE
         os.chdir('D:/abc/dcard')#改變目錄
    except:
         os.chdir('D:/abc/dcard')

    url= 'https://www.dcard.tw/f/makeup'
    header = {
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    page1 = requests.get(url,headers = header)
    web1 =BeautifulSoup(page1.text,"html.parser")#解析器
    # print(web1)
    a=[]
    for i in web1.select('.PostEntry_root_V6g0rd'): #href
        a.append(i.get('href'))
    #print(a)
    for num ,count in zip(a,range(10)):#文章總量
        url =re.findall('https://www.dcard.tw',url)[0]+num#抓第N篇網址
        tow(url,count)
        

