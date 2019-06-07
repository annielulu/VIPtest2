# coding:utf-8
__author__ = 'lenovo'

import  unittest
from ddt import ddt,data,unpack

@ddt
class Mytest1(unittest.TestCase):
    @data(1)
    def test_1(self,value):
        print(value)
        self.assertEqual(value,2)

    @data(2,3,4)
    def test_2(self,value):
        print(value)
        self.assertEqual(value, 2)

if __name__ == '__main__':
    unittest.main()# 自动去找这个类中所有test开头的方法到测试套件。如果想自定义运行的方法则要