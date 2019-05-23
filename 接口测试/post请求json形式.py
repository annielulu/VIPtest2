# coding:utf-8
__author__ = 'lenovo'

# 第一种方式
import requests,json
# 发送请求
urlstr = 'http://httpbin.org/post'
payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}
# 通过json.dumps方法将python字符串转化成json类型
payload = json.dumps(payload)
# 发送请求
r = requests.post(url=urlstr,data=payload)
# 获取结果
print(r.text)
# 返回为json类型，既可以通过r.json方法来查看结果
print(r.json())

# 第二种方式
import requests,json
# 发送post请求
urlstr = 'http://httpbin.org/post'
payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}
# 发送请求，接口请求为json数据，通过json=自动将python对象转变为json类型
r = requests.post(url=urlstr,json=payload)
# 获取结果
print(r.text)
# 返回为json类型，即可以通过r.json方法来查看结果
print(r.json())