# coding:utf-8
__author__ = 'lenovo'


# ----------读取------
# 查找文件路径的方式data右键选Show in Explorer
# 路径支持绝对和相对路径
# 模式：r:读；r+:读写 w:写（覆盖/新建） w+:读写（覆盖/新建） a:追加（没有的时候新建）
# 打开文件open，两个常用参数：文件路径和打开模式
f = open('F:\Code\VIPtest2\data.txt','r')

# 读取文件全部内容，或者读取指定长度字节的数据
print(f.read())
print(f.read(4))
# 读取整行
print(f.readline())
for i in range(5):
    print(f.readline())
# 读取所有行
print(f.readlines())

# ---------写入------
f = open('F:\Code\VIPtest2\data2.txt','r+')
f.write('hello python!\n')
f.write('welcome~')
f.close()

# 作业：只取出data中的数字并写入另外的文件
# 1.读取文件中的所有数据 -- readlines
# 2.从列表中找出含有的数字
#   判断列表中的每一个元素是否含有数字 --- 将列表中的每一个元素（数据的行）取出来，作为一个小的列表
#   判断每一个小的列表是否含有数字 isdigit(),如果是数字，则追加到一个新的列表
# 3.排序，写入

f = open('F:\Code\VIPtest2\data.txt','r')
lines = f.readlines()
# print(lines)
lists = []
for l in lines:
    # print(l)
    s = l.split(',')   # 切片
    # print(s)
    for m in s:
        if m.strip().isdigit():   # 判断是否为数字
            lists.append(m.strip())
        else:
            continue
    for i in range(1,len(lists)):   # 冒泡排序
        for j in range(0,len(lists)-i):
            if lists[j] > lists[j+1]:
                lists[j],lists[j+1] = lists[j+1],lists[j]
print(lists)
f.close()
f1 = open('F:\Code\VIPtest2\data3.txt','r+')
f1.write(str(lists))
f1.close()

# 冒泡排序
# for i in range(1,len(lists)):
#     for j in range(0,len(lists)-i):
#         if lists[j] > lists[j+1]:
#             lists[j],lists[j+1] = lists[j+1],lists[j]











