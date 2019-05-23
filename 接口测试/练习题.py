# coding:utf-8
__author__ = 'lenovo'

import requests
# 发送post请求
urlstr = 'https://www.wanandroid.com/user/login'
# 参数
payload = {'username':'annieliang','password':'123456'}
# 第二步：发送请求
r = requests.post(url=urlstr,data=payload)
# 第三步：获取结果(与fiddler中抓到的请求一致)
print(r.text)
# 查看类型后为字典类型，r.json将response中返回的json处理成了dict
print(type(r.json()))
# 通过dict-key来访问对应的值
print(r.json()['data']['username'])
# 判断是否登录成功（username是否是username）
# 判断返回的json数据是否有登录的用户名或通过正则来获取
if r.json()['data']['username'] == payload['username']:
    print('登录成功！')











