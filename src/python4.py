#!~/Documents/tensorflowVE3/bin/python3

'''
Introduction to Python
REF : Jump to Python / https://docs.python.org/3/tutorial/index.html
'''


class Calculator:
    def __init__(self):
        self.result = 0
        self.operator = ["add", "sub", "mul", "div"]
        print (self.operator)

    def add(self, *args):
        print ("Add operator : ")
        for i in args:
            self.result = self.result + i
            print("%d" %(i), end=" + ")
        print (" = ", end= " ")
        print (self.result)
        return self.result

    def sub(self, *args):
        print ("Sub operator : ")
        for i in args:
            self.result = self.result - i
            print("%d" %(i), end=" - ")
        print (" = ", end= " ")
        print (self.result)
        return self.result

    def mul(self, *args):
        print ("Mul operator : ")
        for i in args:
            self.result = self.result * i
            print("%d" %(i), end=" x ")
        print (" = ", end= " ")
        print (self.result)
        return self.result

    def div(self, *args):
        print ("Div operator : ")
        for i in args:
            self.result = self.result / i
            print("%d" %(i), end=" / ")
        print (" = ", end= " ")
        print (self.result)
        return self.result


calc1 = Calculator()
calc1.add(10, 20, 30)
calc1.mul(2)


class Super_calculator(Calculator):
    def __init__(self):
        super(Super_calculator, self).__init__()
        self.operator.append("integral")
        print (self.operator)

    def integral(self):
        print ("integral x is 0.5x^2")

    def power2(self, num):
        self.result = num
        print (self.result**2)


calcSup = Super_calculator()
calcSup.integral()
calcSup.power2(25.55)

from python3 import func_kwargs

func_kwargs(1, 2, 3,55, name="parkSH", age=222)

'''
['add', 'sub', 'mul', 'div']
Add operator :
10 + 20 + 30 +  =  60
Mul operator :
2 x  =  120
['add', 'sub', 'mul', 'div']
['add', 'sub', 'mul', 'div', 'integral']
integral x is 0.5x^2
652.8025
Hello!!!
30
710
(1, 2, 3)
{'age': 22, 'name': 'parkSH'}
아무 숫자나 입력하세요
33
input is : 33

title : pythontext

format : txt

Life is too short, write in Python
title : pythontext

format : txt

Life is too short, write in PythonLife is too short, write in Python
(1, 2, 3, 55)
{'age': 222, 'name': 'parkSH'}
'''
