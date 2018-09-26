#!~/Documents/tensorflowVE3/bin/python3

'''
Introduction to Python
REF : Jump to Python / https://docs.python.org/3/tutorial/index.html
'''


def printhello():
    print ("Hello!!!")


printhello()


def sum(a, b):
    return a + b


print (sum(10, 20))


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


print (sum_many(10, 20, 30, 50, 600))


def func_kwargs(*args, **kwargs):
    print (args)
    print (kwargs)


func_kwargs(1, 2, 3, name="parkSH", age=22)

while(True):
    number = input("아무 숫자나 입력하세요 \n")
    # isdigit() isalnum() isalpha() isnumeric()
    if number.isdigit() is True:
        print ("input is : %s\n" % (number))
        break
    else:
        continue

import os

cwd = os.getcwd()
file_dir = cwd + "/pythontext.txt"
file_1 = open(file_dir, "r")
while (True):
    # file_1.readlines()
    line = file_1.readline()
    if not line:
        break
    print (line)
file_1.close()

with open(file_dir, 'a') as f:
    f.write("Life is too short, write in Python")

file_1 = open(file_dir, "r")
while (True):
    # file_1.readlines()
    line = file_1.readline()
    if not line:
        break
    print (line)
file_1.close()

'''
Hello!!!
30
710
(1, 2, 3)
{'age': 22, 'name': 'parkSH'}
아무 숫자나 입력하세요
3
input is : 3

title : pythontext

format : txt

title : pythontext

format : txt

Life is too short, write in Python
'''
