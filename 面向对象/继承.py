# coding:utf-8
__author__ = 'lenovo'


# 第一步：继承谁，类中的括号就写谁
# 第二步：继承后，子类就具有父类的所有属性和方法，但是父类不能具备子类的属性和方法
# 第三步：如果父类中没有子类需要的方法，可以在子类中自行定义
# 注意：实例化和调用方法的时候要区分是否需要传参
class Animal:
    def eat(self):
        print('吃饭')
    def drink(self):
        print('喝水')
class Dog:
    def eat(self):
        print('吃饭')
    def drink(self):
        print('喝水')

class Dog(Animal):    # 继承
    def bark(self):
        print('汪汪叫')

class Cat(Animal):
    def catch(self):
        print('抓老鼠')

a = Cat()
a.eat()

# 继承练习：
# 定义一个Teacher类，继承Person类，拥有自身的属性工号gh，自身的方法：teach教课（课程）；
# 1、实现gh为xx的老师，教xx课
# 2、实现gh为xx老师，在xx上班，一月工资xx
# 3、实现名字是xx，工号为xx的老师，吃饭
class Person:
    def __init__(self,name):
        self.name = name
        print('此方法被调用！')
    def eat(self,food):
        print('%s吃%s'%(self.name,food))
    def sleep(self):
        print('睡觉')
class Teacher(Person):
    def __init__(self,gh,salary,name):
        self.gh = gh
        self.salary = salary
        self.name = name
    def teach(self,course):
        print('工号为%s的老师，教%s课'%(self.gh,course))
    def address(self,place):
        print('工号为%s的老师，在%s上班，一月薪资%s'%(self.gh,place,self.salary))
    def eat(self,food):
        print('名字是%s，工号为%s的老师吃%s'%(self.name,self.gh,food))
a = Person('xiaoming')
b = Person('xiaohong')
c = Teacher('66','20000','梁老师')
a.eat('rice')
b.eat('noodle')
c.teach('math')
c.address('beijing')
c.eat('rice')
