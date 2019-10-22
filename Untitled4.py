{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/charles041644/python_code/blob/master/Untitled4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "g6_4gUMsSEoJ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import requests "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Db-3M-_bSIRv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 319
        },
        "outputId": "686a87c0-2a7a-4ac8-eea1-e1bba8d4eae3"
      },
      "source": [
        "from bs4 import BeautifulSoup\n",
        "import getpass\n",
        "import re\n",
        "import requests\n",
        "\n",
        "\n",
        "s = requests.Session()\n",
        "url = 'https://ilearn2.fcu.edu.tw/login/index.php'#開f12看清楚\n",
        "username = input(\"請輸入學號\")\n",
        "password = getpass.getpass(\"請輸入密碼\")#getpass.getpass 裡面的模塊\n",
        "\n",
        "\n",
        "login = s.get(url)#將網頁資料GET下來\n",
        "\n",
        "soup= BeautifulSoup(login.text, \"html.parser\")#將網頁資料>html.parser\n",
        "\n",
        "\n",
        "value =soup.find_all('input',{\"name\":\"logintoken\"})  [0]['value']#提取值，記得+上[0]\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "header = {\n",
        "    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'\n",
        "}#可不用\n",
        "\n",
        "\n",
        "data={\n",
        "    'username':username,\n",
        "    'password':password,\n",
        "    'logintoken':value,   \n",
        "}\n",
        "\n",
        "\n",
        "page = s.post(url, headers=header, data=data)# 其實header不用\n",
        "\n",
        "bs_class = BeautifulSoup(page.text, 'html.parser')\n",
        "\n",
        "\n",
        "\n",
        "courseBox = bs_class.find_all(\"div\",class_='coc-mycurricular coursebox clearfix')#爬蟲 抓取 div底下 有2個 要抓的東西 ，所以先抓最上面的div的 class值\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "for course in courseBox:\n",
        "    try:\n",
        "        courseName = course.find_all('div') [0].find('a').text#已經抓到 上層的div 那分別抓 下層的第一個與第二個div的 a 與span的東西 轉乘text print出來\n",
        "        teacher = course.find_all('div')[1].find('span').text\n",
        "        print(courseName+teacher)\n",
        "    except:\n",
        "        print(courseName)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入學號D0753514\n",
            "請輸入密碼··········\n",
            "1081 軟體工程導論(資訊二甲)[1545]教師: 許懷中\n",
            "1081 通訊與網路概論(資訊二丁)[1563]教師: 洪維志\n",
            "1081 資料結構實習(資訊二丁)[1564]教師: 陳青文\n",
            "1081 資料結構(資訊二丁)[1565]教師: 陳青文\n",
            "1081 離散數學(資訊二丁)[1566]教師: 游景盛\n",
            "1081 密碼學(資訊二合)[1568]教師: 李榮三\n",
            "1081 安全程式設計(網路資安學程資訊三)[2344]教師: 王銘宏\n",
            "1081 日文(一)(應外選修)[3277]教師: 張雪玉\n",
            "1081 服務學習(綜合班)[3586]\n",
            "1081 大二英文(一)(大二英綜)[3733]教師: 林芷瑩\n",
            "1081中級閱讀練習Reading Comprehension Exercises-- Intermediate Level[大二英文][00074][2019/12/13 13:10-17:00 ( 紀104)]教師: 周振權\n",
            "1081背包客英文: 一個人也行 Backpacker English: Let’s hit the road[大二英文][00179][2019/11/30 08:10-12:00 ( 商204)]教師: 吳舜華\n",
            "1081觀光英語會話-出入境、住宿、血拚Tourism English conversation: airport, hotel check in,[大二英文][00208][2019/12/04 17:10-21:00 ( 資電402)]教師: 樊家瑋\n",
            "1081原來這樣就能教英文 English Tutoring[大二英文][00234][2019/11/22 13:10-17:00 ( 人407)]教師: 施惠家\n",
            "1081職場英語會話小劇場Workplace English conversation and role play[大二英文][00294][2019/10/02 17:10-21:00 ( 資電402)]教師: 樊家瑋\n",
            "逢甲大學\\資電學院\\資訊系學生資訊站教師: 陳雅真\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rvIiJH8RSVCb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}