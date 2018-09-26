#!~/Documents/tensorflowVE3/bin/python3

'''
Introduction to Python
REF : Jump to Python / https://docs.python.org/3/tutorial/index.html
'''

int_a = 125
int_b = 99

divide = int_a / int_b
power = int_a ** int_b
print ("int_a / int_b : %f \n" % (divide))
print ("int_a / int_b : %0.2f \n" % (divide))
print ("int_a / int_b : %5.2f \n" % (divide))
print ("int_a POWER int_b : %d \n" % (power))
quotient = int_a // int_b
remainder = int_a % int_b
print ("int_a // int_b : %d \n" % (quotient))
print ("int_a %% int_b : %d \n" % (remainder))

float_a = 1.24
float_b = 4.42e-1
multiply = float_a * float_b
print ("float_a x float_b : %f \n" % (multiply))

str_a = "Hello! world\t"
str_b = str_a + "Python3"
print (str_a * 5 + "\n")
print ("str_a[0] : %s \n" % (str_a[0]))
print ("str_b[-1] : %s \n" % (str_b[-1]))
print ("str_b[0:-1] : " + str_b[0:-1] + "\n")
print ("str_b.count('l') : %d \n" % (str_b.count("l")))
# str.find("sth") if not -> return -1
print ("str_b.find('l') : %d \n" % (str_b.find('l')))
str_c = ","
str_c = str_c.join(str_a)
print ("str_a.join(',') : %s \n" % (str_c))
print ("str_c.split(',') : ", end=" ")
print (str_c.split(','))
'''
to change str_b : python3 -> python2
str_b[-1] = 2 ...? NO
!!!string and tuple are Immutable type!!!
'''

list_a = [1, 2, 3, ["hello", "world"], ["1", ["변태적", "list"]]]
print ("list_a : ", end=" ")
print (list_a)
print ("list_a[-1] : ", end=" ")
print (list_a[-1])
print ("list_a[-1][1][0] : ", end=" ")
print (list_a[-1][1][0])
list_b = [4, "5"]
print ("list_a + list_b : ", end=" ")
list_c = list_a + list_b
print (list_c)
del list_c[3]
print ("del list_c[3] : ", end =" ")
print (list_c)
list_c.append('append')
print ("list_c.append('append') : ", end=" ")
print (list_c)
list_c.reverse()
print ("list_c.reverse() : ", end= " ")
print (list_c)
'''
list - pop / index / count
>>> a = [1,2,3]
>>> a.pop()
3
>>> a
[1, 2]

>>> a = [1,2,3]
>>> a.index(3)
2
>>> a.index(1)
0

>>> a = [1,2,3,1]
>>> a.count(1)
2
'''

tuple_a = ('a', 'b', ('ab', 'cd'))
try:
    del tuple_a[1]
except Exception as exp:
    print (exp)
try:
    tuple_a[1] = "change"
except Exception as exp:
    print (exp)

dict_a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
dict_b = {'name':'ex2', 'phone':'0101234567', 'birth': '1015'}
list_dict = [dict_a, dict_b]
print ("list_dict : ", end=" ")
print (list_dict)
print ("dict_a['phone'] : ", end=" ")
print (dict_a["phone"])
print ("dict_a.items() : ", end=" ")
print (dict_a.items())

var_a = [1, 2, 3, 4]
var_b = var_a
print ("memory var_a : ", end=" ")
print (id(var_a))
print ("memory var_b : ", end=" ")
print (id(var_b))
print ("var_a is var_b ? : ", end= " ")
print (var_a is var_b)

from copy import copy

copy_b = copy(var_a)
print ("memory copy_b : ", end=" ")
print (id(copy_b))
print ("var_a is copy_b ? : ", end= " ")
print (var_a is copy_b)

'''
(tensorflowVE3) parksh@parksh-P35V2:~/Documents/dl_seminar/src$ python python1.py
int_a / int_b : 1.262626

int_a / int_b : 1.26

int_a / int_b :  1.26

int_a POWER int_b : 3927274772238181242476617563989020514380172409999559652089239293749684203777372685168078307229865561821746857252105502810534334888339775122246011859287170761802484371567889542831153448787517845630645751953125

int_a // int_b : 1

int_a % int_b : 26

float_a x float_b : 0.548080

Hello! world	Hello! world	Hello! world	Hello! world	Hello! world

str_a[0] : H

str_b[-1] : 3

str_b[0:-1] : Hello! world	Python

str_b.count('l') : 3

str_b.find('l') : 2

str_a.join(',') : H,e,l,l,o,!, ,w,o,r,l,d,

str_c.split(',') :  ['H', 'e', 'l', 'l', 'o', '!', ' ', 'w', 'o', 'r', 'l', 'd', '\t']
list_a :  [1, 2, 3, ['hello', 'world'], ['1', ['변태적', 'list']]]
list_a[-1] :  ['1', ['변태적', 'list']]
list_a[-1][1][0] :  변태적
list_a + list_b :  [1, 2, 3, ['hello', 'world'], ['1', ['변태적', 'list']], 4, '5']
del list_c[3] :  [1, 2, 3, ['1', ['변태적', 'list']], 4, '5']
list_c.append('append') :  [1, 2, 3, ['1', ['변태적', 'list']], 4, '5', 'append']
list_c.reverse() :  ['append', '5', 4, ['1', ['변태적', 'list']], 3, 2, 1]
'tuple' object doesn't support item deletion
'tuple' object does not support item assignment
list_dict :  [{'birth': '1118', 'name': 'pey', 'phone': '0119993323'}, {'birth': '1015', 'name': 'ex2', 'phone': '0101234567'}]
dict_a['phone'] :  0119993323
dict_a.items() :  dict_items([('birth', '1118'), ('name', 'pey'), ('phone', '0119993323')])
memory var_a :  139986661370824
memory var_b :  139986661370824
var_a is var_b ? :  True
memory copy_b :  139986684993608
var_a is copy_b ? :  False
'''
