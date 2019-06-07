# coding:utf-8
__author__ = 'lenovo'

import unittest
from myfun import *
import HTMLTestRunner

class myTest(unittest.TestCase): # 单元测试类必须继承unittest.TestCase这个类
    def setUp(self):
        print('执行setup方法')
    def tearDown(self):
        print('执行tearDown方法')
    def test_add(self):
        self.assertEqual(add(1,2),3)

if __name__ == '__main__':
    # unittest.main()
    filename = ''
    fp = file(filename,'wb')
    runner = HTMLTestRunner(
        stream = fp
        title = u'百度搜索测试报告'
        description = u'用例执行情况'
    )
runner.run(suite)
fp.close()



# 1、语法：
# 首先引入HTMLTestRunner包
# import HTMLTestRunner
# 用法：
# 1----------#定义个报告存放路径
# filename = 'C:\\test_object\\report\\result.html' 
# 2----------#定义一个文件名，以写方式打开
# fp = file(filename, 'wb') 
# 3----------#定义测试报告
# runner =HTMLTestRunner.HTMLTestRunner(
#      stream=fp,
#      title=u'百度搜索测试报告',
#      description=u'用例执行情况：')
# 4----------#运行测试用例
# runner.run(suite)
# 5----------#关闭报告文件
# fp.close()