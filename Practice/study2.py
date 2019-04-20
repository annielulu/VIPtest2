#coding:utf-8
__author__ = 'lenovo'
# try:
#     a = int(input('please input a num:'))
#
#     if a > 0:
#         a += 10
#     elif a == 0:
#         a += 20
#     else:
#         a += 30
#     print(a)
# except ValueError:
#     print('请输入数字！')

# n = 100
# while n > 0:
#     a = int(input('please input a num:'))
#     if a >= 90 and a <= 100:
#         print('等级为A')
#     elif a >= 80 and a < 90:
#         print('等级为B')
#     elif a >=70 and a < 80:
#         print('等级为C')
#     elif a >= 60 and a < 70:
#         print('等级为D')
#     else:
#         print('等级为E')
#
#     n -= 1

# #求1-100的和
# a = 0
# n = 1
# while n <= 100:
#     a = a + n
#     n += 1
# print(a)

# for i in [1,2,3,4]:
#     print(i,'ok')
#
# for i in range(1,10):
#     print(i)

#打印1-1000的基数
# for i in range(1,1000,2):
#     print(i)
# #打印1-5的数字遇到3的时候不打印
#  for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)
# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)

#求10的阶乘
a = 1
n = 1
while n <= 10:
    a = a * n
    n += 1
print(a)
#求100以内能被3整除的数
n = 1
for i in range(1,100):
    if i % 3 == 0:
        print(i)
    else:
        n += 1
#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
m = [1,2,3,4,3,4,2,5,5,8,9,7]
m = list(set(m))
print(m)
#求斐波那契数列 1 2 3 5 8 13 ……
n = 0
a = 1
b = 2
c = 3
while n < max:
    print(a)
    a + b = c


    n += 1



