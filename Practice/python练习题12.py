# coding:utf-8
__author__ = 'lenovo'

# 1、打印小猫爱吃鱼，小猫要喝水
class Animal():
    def __init__(self,name):
        self.name = name
        print('此方法被调用')
    def eat(self,food):
        print('%s爱吃%s'%(self.name,food))
    def drink(self,drinks):
        print('%s要喝%s'%(self.name,drinks))
a = Animal('小猫')
a.eat('鱼')
a.drink('水')

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        print('此方法被调用')
    def person1(self):
        print('%s的体重是%s'%(self.name,self.weight))
    def run(self):
        print('%s爱跑步,每次跑步会减肥%s'%(self.name,self.weight))
    def eat(self,food):
        print('%s爱吃%s,每次吃东西体重会增加%s'%(self.name,food,self.weight))
    def person2(self):
        print('%s的体重是%s'%(self.name,self.weight))
a = Person('小明','75kg')
b = Person('小明','0.5kg')
c = Person('小明','1kg')
d = Person('小美','45kg')
a.person1()
b.run()
c.eat('东西')
d.person2()














