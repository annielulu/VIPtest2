# coding:utf-8
__author__ = 'lenovo'

# import re
# result1 = re.match('www', 'www.runoob.com').span()  # 在起始位置匹配
# print(result1)
# result = re.match('com', 'www.runoob.com')         # 不在起始位置匹配
# print(result)

import re
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
#
# result = re.search('www','www.baidu.com')
# print(result)
# print(result.group(0))

pattern = re.compile(r'\d')
result = pattern.findall('1jdkahf3jdhad4')
print(result)



