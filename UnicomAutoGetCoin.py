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
            'Cookie': 'channel=GGPD; city=034|358; devicedId=FE0172BD-1BF5-4774-BC31-DD77360C3214; c_sfbm=234g_00; logHostIP=null; mobileService1=1Y4RfyPLLL0tvLpGnRK2QL5gQg1bDWSjnLvZ2RWKtWBWYywxWQpL!899433259; mobileServiceAll=dfd8b2e9f03c6c97f078fed5a9b73a86',
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
        print( ' coin: ' + urllib2.urlopen(req5).read().decode('utf-8'))
        data2={'stepflag':'22'}
        for x in range(3):
        	r = urllib2.Request("http://act.10010.com/SigninApp/mySignin/addFlow",data=data2)
        	
if __name__ == '__main__':

    user = Qiandao()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = timestamp+"&simCount=1&version=iphone_c@7.0403&mobile=aMawi%2B3MkY4NRaqS7QTmYi8TjvW8K9wNN%2FQKGunt%2BfMXVOzLBYy4SXVKpgmzNpRHEAYhXnvuOAnsR%2FavuhMmixJ8tvEY0XGOYRW%2BzQWjitbpdU%2BFEGsy1hCbhNvgDSiB6PNyO2atgasvd7L31G1z7S9LTDThgR0%2Fx2unpy1J440%3D&netWay=4G&token_online=&appId=d599e6c4238cb46a76affdd536358ebc3b008adeb7a0be09a9aae646ec829d2fb382ca25f1581cf840cbcdbfe0b57755f2165c6ee223c0734de392497ba30b0c28979bbed7cfcf836234e690b7f7ee10e8ecfff5d45ff54bb5e2b9bae924e5cc&deviceId=9927387fe8e271391ac409610cfd22e54948be639c61ee78ce08f2acbe823a1c&isRemberPwd=false&pip=10.99.16.240&password=DGLHJeUJy4SKFG0N8EODC0JbtgbRKSfnICwxZ0ZgRkRElDlERJQ%2Fq9dcE3vzf%2Bv6h7NFIAzjO4O%2Bx9R8vp3mt1TaiLb6Q9LdPtTntcwHAH9qEFa%2FQbpFTggwuyjmC0vswD2J7wwNZkZs0M0P34n%2FUNgf%2FGiGRBvD3gpYo%2FYL1uU%3D&deviceOS=13.6&deviceBrand=iphone&deviceModel=iPhone&remark4=&keyVersion=1&deviceCode=FE0172BD-1BF5-4774-BC31-DD77360C3214"

    user.sign(data)
