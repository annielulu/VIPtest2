# coding:utf-8
# __author__ = 'lenovo'

# 第一种调用方式--只能导入，名称
import Mymodule # 右键practice-->mark directory as->resource root(将当前路径加入python查找的默认路径)
# 如果通过import调用，使用包内的方法需要通过包名.函数名的形式
Mymodule.fun1()

# 第二种调用方式--通过from .. import的形式导入，from后面只能跟包和模块名，不能跟函数名，import后面跟函数或者类名
from Mymodule import fun1
# 通过from-import的形式可以直接使用函数名
fun1()
fun2()

# 通过import* 可以导入多个函数
from Mymodule import *