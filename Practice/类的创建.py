# coding:utf-8
__author__ = 'lenovo'

# 类的定义
class Person:
    # 类属性/方法 -- 初始化方法，类中必须存在的且在实例化过程中自动被调用的方法（定义属性）
    def __init__(self,name):
        self.name = name
        print('此方法被调用！')

    def eat(self,food):
        print('%s吃%s'%(self.name,food))
        # print(self.sleep()) #调用别的方法需要加self
    def sleep(self):
        print('睡觉')

# 类的调用第一步：实例化（创建一个对象：变量名=类名()）---是否需要传参就看__init__方法中除了self是否还有其他参数
a =  Person('xiaoming')
b = Person('xiaohong')
# 类的调用第二步：调用类中的方法（实例名.方法名()） ---是否需要传参就看该方法中除了self是否还有其他参数
a.eat('rice')
b.eat('noodle')


# 练习：定义一个学生类，内部含有一个方法：study，实现打印：XX学习xx课程
class person():
    def __init__(self,name):
        self.name = name

    def study(self,course):
        print('%s学习%s'%(self.name,course))

a = person('xiaoming')
a.study('math')

# 定义一个类名：Student—学生、类内部含有一个属性：sno—学号，一个方法：study—学习，
# 实现打印：学号为xx的学生，学习xx课程
class Student():
    def __init__(self,sno):
        self.sno = sno

    def study(self,course):
        print('学号为%s的学生,学习%s的课程'%(self.sno,course))

a = Student('6')
a.study('math')







