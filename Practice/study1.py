#coding:utf-8
__author__ = 'lenovo'

'''
#变量
a = 5
print(a)
#元组
'''
'''
s = [1,2,3]
print(s)
m = (1,2,3)
print(m)
'''
'''
#字典
d ={'a':1,'b':2}
print(d)
print(type(a))


a = 5
b = 2.5
c = 'happy'
print(a,b,c)

message = "let's go"
print(message)

a = input('请输入：')
print(a)
'''

# a,b,c,d,e = input('请输入5个数字：').split()
# print('输出结果为：',a,b,c,d,e)
# a,b,c,d,e = input('请输入5个数字：').split()
# print(('%s,%s,%s,%s,%s')%(a,b,c,d,e))

#元组 - 不可变
# s = (1,2.5,'happy')
# print(s)
# print(type(s))

# #列表 - 可变
# m = [1,2.5,'happy']
# print(m)
# print(type(m))
# print(m[2])

# #定义一个1-10的列表
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a)
# print(a[3],a[4],a[5])
# print(a[6:9:1]) #6为下限下标，9为上限，1为步长（隔几个逗号）
# print(a[2:9:2])
# print(a[1:8:2])
# print(a[-1]) #输出最后一个数
# print(a[3::]) #省略代表到最后
# print(a[:5:])
# print(a[0::2]) #输出所有基数
# print(a[1::2]) #输出所有偶数

# #练习：定义一个1-9的元组list，1、输出倒数第3个元素；2、输出值468
# a = (1,2,3,4,5,6,7,8,9)
# print(a[-3])
# print(a[3],a[5],a[7])

# #定义一个1-999的元组
# a = list(range(1,1000))
# print(a)

# a = int(input('please input a num:'))
# print(a)

# #倒序输出
# a = [1,2,3,4,5]
# a.reverse()
# print(a)
# #对原列表进行排序
# a = [6,2,5,4,3,1]
# a.sort()
# print(a)
# #不改变原来元组的值，只返回一个排序结果
# a = [6,2,5,4,3,1]
# print(sorted(a))
# print(a)
#在4的前面插入元素a
# a = [6,2,5,4,3,1]
# a.insert(3,'a')  #3是4的下标
# print(a)
# #追加-在末尾追加
# a = [6,2,5,4,3,1]
# a.append(11)
# print(a)
#连接2个列表
a = [6,2,5,4,3,1,2,4,2]
# b = ['a','b','c']
# a.extend(b)
# print(a )
# #删除5这个元素
# a.pop(2)
# print(a)
# #删除元素第一次出现的值
# a.remove(2)
# print(a)
# #返回元素2在列表中出现的次数
# print(a.count(2))
# print(max(a))
# print(min(a))
# print(len(a))  -- 元素的个数
#删除下标为1的元素
# del a[1]
# print(a)
# #返回元素的下标
# print(a.index(4))

#列表[11,13,5,7,0,56,23,34,72]
#求列表中的最大值、最小值及列表中一共有几个元素
# a = [11,13,5,7,0,56,23,34,72]
# print(max(a))
# print(min(a))
# print(len(a))
# #获取56在元素中的位置
# print(a.index(56))
# #追加元素7
# a.append(7)
# print(a)
# #删除元素0
# del a[4]
# print(a)
# #排序列表，由大到小
# a.sort()
# a.reverse()
# print(a)
# #将列表[66,67,68]与原列表组合
# b = [66,67,68]
# b.extend(a)
# print(b)

#元组不可增删改

#集合：无序，且不重复，
# 不能通过下标引用
#操作：添加：s.add(n)--向集合s添加元素n
#删除：s.remove(n) -- 删除集合中的元素n，如果元素不存在，报keyerror异常
#删除：descard（） --删除集合中的元素n
#清空 - s.clear() -- 清空集合
#in 和not in --用于检查是否在集合中
# s = [4,1,2,3,2,1]
# m = set(s) #先转化成集合
# print(m)
# m = list(set(s)) #再转化成列表，列表是有序的有下标
# print(m)

s = {'a':1,'b':2,'c':3}
print(s['c'])
s['d'] = 50
# print(s)
print(s.keys())
print(type(s.keys()))
print(list(s.keys()))
print(s.values())
print(type(s.values()))
print(list(s.values()))
# print(s.values())
# print(s.items())
# print(s.clear())
# del s['key']
# print(s)

