# coding:utf-8
__author__ = 'lenovo'

# 第一步：导入包
import requests
# 第二步：发送get请求
urlstr = 'https://www.wanandroid.com/blog/show/2'
r = requests.get(url=urlstr)   # r = response
# 第三步：获取结果
print(r.text)

# 携带参数
# 导入包
import requests
# 发送get请求
urlstr = 'https://www.wanandroid.com/article/query'
param = {'k':'Android'}  # 参数
r = requests.get(url=urlstr,params=param)
# 获取结果
print(r.text)
print(r.status_code)


# 携带参数
import requests
# 发送get请求，将参数直接携带在url中
urlstr = 'https://www.wanandroid.com/article/query?key=Android'
r = requests.get(url=urlstr)
# 获取结果
print(r.text)
print(r.status_code)  # 打印出状态码
print(r.headers)   # 打印出header信息
