# coding:utf-8
__author__ = 'lenovo'

# try .. except --已知异常类型
def calc(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('除数不能为0！')

a = int(input('-'))
b = int(input('-'))

calc(a,b)

# try .. except --未知异常
def calc(a,b):
    try:
        print(a/b)
    except Exception:   # BaseException(https://www.cnblogs.com/zln1021/p/6106185.html)
        print('除数不能为0！')

a = int(input('-'))
b = int(input('-'))

calc(a,b)

# 多重异常 -- 挨个匹配except后的异常
def calc(a,b):
    try:
        print(a/b)
    except NameError:
        print('该对象未申明')
    except ZeroDivisionError:
        print('除数不能为0')

a = int(input('-'))
b = int(input('-'))

calc(a,b)

# 最终处理 -- 不管有没有抛出异常都执行finally
def calc(a,b):
    try:
        print(a/b)
    except NameError:
        print('该对象未申明')
    except ZeroDivisionError as msg:
        # print(msg)
        print('除数不能为0',msg)
    finally:
        print('程序执行完毕')

a = int(input('-'))
b = int(input('-'))
calc(a,b)


# 抛出异常 -- 必须为exception的子类
raise TypeError('类型错误')

# else -- 程序没有抛出异常，继续执行else语句
def calc(a,b):
    try:
        print(a/b)
    except NameError:
        print('该对象未申明')
    except TypeError as msg:
        print(msg)
    else:
        print('程序执行完毕！')

a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))
calc(a,b)

def calc(a,b):
    try:
        print(a/b)
    except NameError:
        print('该对象未申明')
        # 查看异常后不做处理继续抛出异常
        raise
    except ZeroDivisionError as msg:
        # print(msg)
        print('除数不能为0',msg)
    else:
        print('程序执行完毕')

a = int(input('-'))
b = int(input('-'))
calc(a,b)

# name没有定义，type异常，并抛出是何种异常
def calc(a,b):
    try:
        print(a/b)
    except NameError as msg:
        print('该对象未申明',msg)
        raise
    except TypeError as msg:
        print(msg)
        raise
    else:
        print('程序执行完毕！')

a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))
calc(a,b)



