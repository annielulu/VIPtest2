# coding:utf-8
__author__ = 'lenovo'

'''
1.分支：if分支/if...else分支/if...elif嵌套
2.练习
'''

# 例子：a>0,则加10，a=0,加20，a<0,加30，只能输入数字
try:
    a = int(input('please input a num:'))
    if a > 0:
        a += 10
    elif a == 0:
        a += 20
    else:
        a += 30
    print(a)
except ValueError:
    print('请输入数字！')

# 例子：输入一个数，判断该数的等级：90-100：等价为A……60以下：等级为E
n = 100
while n > 0:
    a = int(input('please input a num:'))
    if a >= 90 and a < 100:
        print('等级为A')
    elif a >= 80 and a < 90:
        print('等级为B')
    elif a >=70 and a < 80:
        print('等级为C')
    elif a >= 60 and a < 70:
        print('等级为D')
    else:
        print('等级为E')
    n -= 1

# 练习1：求1-100的和
a = 0
n = 1
while n <= 100:
    a = a + n
    n += 1
print(a)

# 例子：依次打印列表中的元素
for i in [1,2,3,4]:
    print(i,'ok')

# 例子：打印1-10的数字
for i in range(1,10):  #不包含10
    print(i)

# 练习2：打印1-1000的奇数
for i in range(1,1000,2):
    print(i)

# 例子：打印1-5的数字遇到3的时候不打印
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# 例子：打印1-5的数字，遇到3时跳出循环
for i in range(1,6):
    if i == 3:
        break
    print(i)

# 练习3：求10的阶乘
a = 1
i = 1
while i <= 10:
    a = a * i
    i += 1
print('10的阶乘为：',a)

# 计算任意数的阶乘
x = 1
y = int(input("请输入要计算的数:"))
for i in range(1, y + 1):
   x = x * i
print('输入数的阶乘为：',x)

# 练习4：求100以内能被3整除的数
n = 1
for i in range(1,100):
    if i % 3 == 0:
        print(i)
    else:
        n += 1

# 练习5：列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
m = [1,2,3,4,3,4,2,5,5,8,9,7]
m = list(set(m))
print(m)

# 练习6：求斐波那契数列：1 1 2 3 5 8 13 ……
a = 1
b = 1
i = 0   # i=2
if i == 1:
    print(a,end=',')
else:
    print(a,end=',')
    print(b,end=',')
    while i < 10:
        c = a + b
        print(c,end=',')
        a = b
        b = c
        i += 1

# 求斐波那契数列：1 1 2 3 5 8 13 ……,并以列表的形式输出
a = 1
b = 1
i = 0
lists = []
if i == 1:
    print(a)
else:
    lists.append(a)
    lists.append(b)
    while i < 10:
        c = a + b
        lists.append(c)
        a = b
        b = c
        i += 1
    print(lists)

# 输出任意项的斐波那契数列
array = int(input("请输入你需要多少项斐波那契数列："))
a = 1
b = 1
i = 2
if array <= 0:
    print("请输入一个大于等于1的正整数！")
elif i == 1:
    print("斐波那切数列为：")
    print(a,end=',')
else:
    print("斐波那切数列为：")
    print(a,end=',')
    print(b,end=',')
    while i < array:
        c = a + b
        print(c,end=',')
        a = b
        b = c
        i += 1

# 作业：输出100以内的所有质数(2、3、5、7、11、13、17、19...)（只能被1和其本身整除的数）
lists = []
i = 2
for i in range(2,100):
    n = 2
    for n in range(2,i):
        if i % n == 0:
            break
    else:
        lists.append(i)
print(lists)


