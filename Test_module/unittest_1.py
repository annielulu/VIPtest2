# coding:utf-8
__author__ = 'lenovo'

import unittest
from Mysum import My_func

class Mytest(unittest.TestCase):

    def setUp(self):
        print('初始化测试环境')
    def test_sum(self):
        x = int(input('>---'))
        y = int(input('>--'))
        re = My_func.add(x,y)
        if re == 3:
            print('测试通过')
        else:
            print('测试失败')
    def tearDown(self):
            print('清理测试环境')
if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Mytest.test_sum())
    # runner = unittest.TextTestRunner