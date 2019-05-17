# coding:utf-8
__author__ = 'lenovo'

class Dog(object):
    def print_self(self):
        print('大家好，我是xxx')

class Xiaotq(Dog):
    def print_self(self):
        print('hello,everyboby,我是xxx')

def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

# 多态的关键在于，同样是调用相同的方法，但是完成的内容却不同，普通狗的自我介绍是与哮天犬的自我介绍不一样
introduce(dog1)
introduce(dog2)