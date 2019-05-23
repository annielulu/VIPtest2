# coding:utf-8
__author__ = 'lenovo'

# 导入包
import requests
# 发送post请求
urlstr = 'https://www.wanandroid.com/user/login'
# 参数
data = {'username':'annieliang','password':'123456'}
r = requests.post(url=urlstr,data=data)
# 获取结果(与fiddler中抓到的请求一致)
print(r.text)
print(type(r.json())) # 查看类型
# 通过dict-key来访问对应的值
print(r.json())
print(r.json()['errorCode'])
print(r.json()['data']['username'])



