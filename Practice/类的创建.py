# coding:utf-8
__author__ = 'lenovo'

# 类的定义
# class Person:
#     # 类属性
#     # name = 'xiaoming'
#
#     # 实例属性
#     # 初始化方法，类中必须存在的且在实例化过程中自动被调用的方法（定义属性）
#     def __init__(self,name):
#         self.name = name
#         print('此方法被调用！')
#
#     def eat(self,food):
#         print('%s吃%s'%(self.name,food))
#         # print(self.sleep()) #调用别的方法需要加self
#     def sleep(self):
#         print('睡觉')
#
# # 类的调用第一步：实例化（创建一个对象：变量名=类名()）
# a =  Person('xiaoming')
# # 类的调用第二步：调用类中的方法（实例名.方法名()）
# a.eat('rice')

# 练习：定义一个学生类，内部含有一个方法：study，实现打印：XX学习xx课程
# class person():
#     def __init__(self,name):
#          self.name = name
#
#     def study(self,course):
#         print('%s学习%s'%(self.name,course))
#
# class student(person):
#     def __init__(self,gh,name):
#         self.gh = gh  # gh是工号的意思
#         self.name = name
#
#     def teach(self,course):
#         print('工号为：%s的老师教%s课'%(self.gh,course))
#         print('工号为：%s的老师教%s课'%(self.name,course))
#
#
# a = person('xiaoming')
# a.study('maths')
#
# a = teach(98,'xiaohong')
# a.teach('math')

# 继承练习：
# 定义一个Teacher类，继承Person类，拥有自身的属性gh，自身的方法：teach教课（课程）；
# 1、实现gh为xx的老师，教xx课
# 2、实现gh为xx老师，在xx上班，一月工资xx
# 3、实现gh吃饭

# 第一步：继承谁，类中的括号就写谁
# 第二步：集成后，子类就具有父类的所有属性和方法，但是父类不能具备子类的属性和方法
# 第三步：如果父类中没有子类需要的方法，可以在子类中自行定义
# 注意：实例化和调用方法的时候要区分是否需要传参


