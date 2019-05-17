# coding:utf-8
__author__ = 'lenovo'

class Animal:
    def eat(self):
        print('吃饭')
    def drink(self):
        print('喝水')

class Dog(Animal):
    def bark(self):
        print('汪汪叫')

class Xiaotq(Dog):
    def fly(self):
        print('飞翔')
    def bark(self):
        print('哮天犬狂叫')
        # 第一种调用被重写的方法，父类的名字.方法名()
        Dog.bark()
        # 第二种
        super().bark()

a = Xiaotq()
a.fly()
a.bark()
# 子类可以拥有父类的功能
a.eat()

