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

# 3、摆放家具
# 需求：
# 1）房子有户型，总面积和家具名称列表,新房子没有任何的家具
# 2）具有名字和占地面积，其中
# 床：占4平米
# 衣柜：占2平面
# 餐桌：占1.5平米
# 3）将以上三件家具添加到房子中
# 4）打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表



# 4.士兵开枪
# 需求：
# 1）士兵瑞恩有一把AK47
# 2）士兵可以开火(士兵开火扣动的是扳机)
# 3）枪 能够 发射子弹(把子弹发射出去)
# 4）枪 能够 装填子弹 --增加子弹的数量








