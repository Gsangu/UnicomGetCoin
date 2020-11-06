### UnicomGetCoin


#联通营业厅签到领积分


   #更新日志
   
      #新增七日4GB流量包获取


#使用方法

  一、自己挂服务器

        只需下载py文件，然后按照下面的操作抓包，最后将py文件倒数第二行的sys.argv[1]替换成抓包得到的cookie即可。
  
  二、利用github的workflow自动运行

        首先fork该项目，然后按照下面的操作抓包，进入setting里面找到secret，添加一个名为COOKIE的secret，将抓包到的cookie复制进去即可。
  
 
 #抓包方法及内容
    
    手机营业厅退出登陆，开启抓包软件，登录手机营业厅
    
    查找网址为 https://m.client.10010.com/mobileService/login.htm 的记录，找到请求文本，从&sim开始到最后后的内容就是所需要的
    
    具体内容见下图
    
   ![Image Text](https://github.com/QiuYueBaiJXW/UnicomGetCoin/blob/master/Photo/A86CC0F6-E719-47C2-9087-AA428FC88C00.jpeg?raw=true)
  
  
  
 #无限期To Do
 
     1.每日自动抽奖三次
     
     2.改进登录方式，取消抓包登录，改用账号密码登录
     
     3.还没想好，有啥好的想法欢迎issue。

    
  #免责申明
    
    该项目仅供学习使用，严禁用于商业用途，由此造成的一切后果，本人概不负责。
