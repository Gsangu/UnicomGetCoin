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
        req5 = urllib2.Request("https://act.10010.com/SigninApp/signin/getIntegral")
        print( ' 积分情况: ' + urllib2.urlopen(req4).read().decode('utf-8'))


if __name__ == '__main__':

    user = Qiandao()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = timestamp+"XXXXXXXXXXXX双引号中的内容换成抓包的结果reqtime=xxxx-xx-xx xx:xx:xx后面的内容XXXXXXXXXXX"
    user.sign(data)
