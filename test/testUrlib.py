# -*- coding = utf-8 -*-
# @Time : 2021/4/2 9:19
# @Author : brilliantZC
# @File : testUrlib.py
# @Software : PyCharm

import urllib.request,urllib.error
import urllib.parse
# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8的解码

# 获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"python"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))

# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!!")

# response = urllib.request.urlopen("https://baidu.com")
# print(response.status)
# print(response.getheaders())

# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name":"eruic"}),encoding="utf-8")
# rep = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(rep)
# print(response.read().decode("utf-8"))

url = "https://www.douban.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}
rep = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(rep)
print(response.read().decode("utf-8"))


