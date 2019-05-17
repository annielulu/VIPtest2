# coding:utf-8
__author__ = 'lenovo'

# 4.士兵开枪
# 需求：
# 1）士兵瑞恩有一把AK47
# 2）士兵可以开火(士兵开火扣动的是扳机)
# 3）枪 能够 发射子弹(把子弹发射出去)
# 4）枪 能够 装填子弹 --增加子弹的数量
class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None
    def __str__(self):
        return '%s士兵的枪为%s' % (self.name, self.gun)
    def fire(self):
        if self.gun == None:
            print('士兵还没有枪')
        else:
            self.gun.shoot()
class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0
    def __str__(self):
        return '%s的子弹有%s颗' % (self.model,self.bullet_count)
    def shoot(self):
        if self.bullet_count < 1:
            print('没有子弹了，请补充子弹再射击')
        else:
            self.bullet_count -= 1
            return self.bullet_count
    def add_bullet(self, count):
        if self.bullet_count >= 50:
            print('子弹已经装满，不可再加')
        else:
            self.bullet_count += count
ryan = Soldier('Ryan')
AK47 = Gun('AK47')
AK47.shoot() # 此时没有子弹不能射击
AK47.add_bullet(50) # 加50发子弹
AK47.shoot()
print(AK47)
ryan.gun = AK47
ryan.fire()
print(ryan)
print(AK47)
