# coding=utf-8
# author: pbbqdd、wfion
# modify: QiuYueBai

import http.cookiejar
import json
import os
import sys
import urllib.request as urllib2
import ssl
import urllib
import datetime
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
class Qiandao():

    def __init__(self):
        self.cookie = http.cookiejar.CookieJar()
        self.handler = urllib2.HTTPCookieProcessor(self.cookie)
        opener = urllib2.build_opener(self.handler)
        urllib2.install_opener(opener)


    def sign(self,data):
        global a
        headers = {
            'Host': 'm.client.10010.com',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'User-Agent': 'ChinaUnicom4.x/230 CFNetwork/1128.0.1 Darwin/19.6.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Length': '910'
        }
        data = data.encode('utf-8')
        req2 = urllib2.Request("http://m.client.10010.com/mobileService/login.htm",headers=headers)
        req2 = urllib2.urlopen(req2,data)
        if req2.getcode() == 200:
            print('login success!')
        try:
            for item1 in self.cookie:
                if item1.name == 'a_token':
                    a = item1.value
        except:
            print("cant get cookies")
        req3 = urllib2.Request("https://act.10010.com/SigninApp/signin/querySigninActivity.htm?token=" + a)
        if urllib2.urlopen(req3).getcode() == 200:
            print('querySigninActivity success!')
        req4 = urllib2.Request("https://act.10010.com/SigninApp/signin/daySign", "btnPouplePost".encode('utf-8'))
        if urllib2.urlopen(req4).getcode() == 200:
            print('daySign success!')
        req5 = urllib2.Request("https://act.10010.com/SigninApp/signin/getGoldTotal")
        print( ' coin: ' + urllib2.urlopen(req4).read().decode('utf-8'))


if __name__ == '__main__':

    user = Qiandao()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = timestamp+"&simCount=1&version=iphone_c@7.0403&mobile=e1%2BPKn7E95gRQCPErqMts1dwdhOCtOpE422oa8wKXps7ZwdXXbE%2BIrUhNtWIAJoWtUYnDvXVnNSV3xgcbkR61bxTHMo6Vlm5%2BfOz531CAvppJeExhHmk3yEdOndR7VL1Sn2XrezLMHmxCqb8kQVCJ2bqJtrISRWJ%2BPcWTCDuH%2F8%3D&netWay=wifi&isRemberPwd=false&appId=af8ceac06275e6af2826a3cf6ea168d620b2ae3115fa1d53f024b2f4fc95d3fa5ceb3b0469fd7d4c95d5cae18e8ce669914a9973c879f1ddc0a1810e61e6f2c3a15ecda8dfee05df77c2450bcd609f2ad487820d385e47bc148742887a0c25dd&deviceId=dd3ce2aba74aa1c7f9ff944b8701bd64b92508a0a2ab0ac501a3752d13121af2&pip=192.168.0.102&password=hwZYb%2BQZLIRnWvkR3UZuEJtNVemBXZ6rWWNEsbcDgRq6UT7%2FtXUxk67M5PmQ5cJNl7KQngqdHnIC%2FFVrHiUbLzbezErNFNevXwuhMXjR%2F1%2BFZF9OmOo%2BpYlf9KJADi1VW4KUp3QbKFnZuRGYhCua2Jj2e1AhhmAmvdbyORMyKgI%3D&deviceOS=13.6&deviceBrand=iphone&deviceModel=iPhone&remark4=&keyVersion=&deviceCode=2D55D64A-28B6-48C8-BF6B-0B0980136C01"
    user.sign(data)
