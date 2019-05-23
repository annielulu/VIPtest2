# coding:utf-8
__author__ = 'lenovo'

# 第一步：导入包
import requests
# 发送get请求
urlstr = 'https://www.wanandroid.com/blog/show/2'

header = {'User-Agent':'Mozzilla/5.0'}
cookie = {'JSESSIONID':'3E08EBE7538380CE432C7FEA74244011'}

r = requests.get(url=urlstr,headers=header)
# 获取结果
print(r.text)
print(r.headers)
print(r.cookies)


