# coding:utf-8
__author__ = 'lenovo'

# 3、摆放家具
# 需求：
# 1）房子有户型，总面积和家具名称列表,新房子没有任何的家具
# 2）具有名字和占地面积，其中
# 床：占4平米
# 衣柜：占2平面
# 餐桌：占1.5平米
# 3）将以上三件家具添加到房子中
# 4）打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
class HouseItem():
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return '[%s]占地 %.2f' % (self.name, self.area)
class House():
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area # 剩余面积
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return ('户型:%s\n总面积:%.2f[剩余:%.2f]\n家具:%s' % (self.house_type, self.area, self.free_area, self.item_list))
    def add_item(self, item):
        # 1.判断家具的面积
        if item.area > self.free_area:
            print('%s的面积太大，无法添加' % item.name)
        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area
# 1.创建家具对象
bed = HouseItem('bed', 4)
yg = HouseItem('yg', 2)
table = HouseItem('table', 1.5)
# 2.创建房子对象
my_house = House('两室一厅', 100)
# 3.添加家具
my_house.add_item(bed)
my_house.add_item(yg)
my_house.add_item(table)
print(my_house)

