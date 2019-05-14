# coding:utf-8
__author__ = 'lenovo'

# 定义函数calc - 无参无返回值
def calc():
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    c = a + b
    # print('结果为：',c)
    print('结果为：%d'%c)
# 调用
calc()

def calc():
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    c = a + b
    return c

# 调用
# print(calc())
result = calc()
print(result)


def calc(x,y):
    c = x + y
    return c

a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))

result = calc(a,b)
print(result)

# 位置参数
def person(name,sex):
    sex_dict = {1:'先生',2:'女士'}
    print('hello %s %s,welcome~'%(name,sex_dict.get(sex,'女士')))
person('baby',2)

# 默认参数指向可变对象时
def add_end(L = []):
    L.append('end')
    return L

print(add_end())
print(add_end())

# 默认参数指向不变对象时
def add_end(L = None):
    if L is None:
        L = []
    L.append('end')
    return L

print(add_end())
print(add_end())

def calc(*numbers):
    print(*numbers)
    print(numbers)
    sum = 0
    for n in numbers:
        sum += n
        return sum
print(calc(1,2))


def calc(*args):
    print(*args)    # *args打印出来是一个一个的整型的数
    print(args,type(args))   # args默认保存为元组，打印出来是一个元组
    for i in args:
        print('传入的值分别为：',i)

# 可变参数传参形式1 - 常用（通过引用的方式必须带*）
m = [1,2,3]
calc(*m)

n = (3,4,5)
calc(*n)

# 可变参数传参形式2
calc(1,2,3)



def person(name,age,**kwargs):
    print('name',name,'age',age,kwargs)
    print(kwargs,type(kwargs))

person('xiaoming',21,sex = 'male',color = 'blue')
person('xiaoming',21)  # 可变参数和关键字参数可以不传
person('xiaoming',21,sex = 1)
person('xiaoming',21,sex = 'male')

def person(name,age,**kwargs):
    print('name',name,'age',age,kwargs)

extra = {'city':'beijing','job':'Engineer'}
person('xiaoming',25,**extra)

# 设计一个计算器，输入两个数，自动实现加减乘除
x = int(input('请输入第一个数：'))
y = int(input('请输入第二个数：'))
def add():
    z = x + y
    return z
def sub():
    z = x - y
    return z
def mul():
    z = x * y
    return z
def div():
    z = x / y
    return z

print('两数相加为：',add())
print('两数相减为：',sub())
print('两数相乘为：',mul())
print('两数相除为：',div())

# 进阶：设计一个计算器，输入两个数，根据用户输入的计算符号自动实现加减乘除
def calc():
    x = int(input('请输入第一个数：'))
    y = int(input('请输入第二个数：'))
    z = input('请输入运算符号：+ - * /:')
    if z == '+':
        result = x + y
        print('两数相加为：',result)
    elif z == '-':
        result = x - y
        print('两数相减为：',result)
    elif z == '*':
        result = x * y
        print('两数相乘为：',result)
    elif z == '/':
        try:
            result = x / y
            print('两数相除为：',result)
        except ZeroDivisionError:
            print('除数不能为0！')
    else:
        print('运算符号输入错误，请重新输入！')
calc()

