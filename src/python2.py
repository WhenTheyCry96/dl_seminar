#!~/Documents/tensorflowVE3/bin/python3

'''
Introduction to Python
REF : Jump to Python / https://docs.python.org/3/tutorial/index.html
'''

money = 1
print ("money = ", end=" ")
print(money, end=" ")
print(type(money))
if money == 1:
    print ("money == 1 (int)")
else:
    pass
if money is 1:
    print ("money is 1 (int)")
else:
    pass

print("\n")

money = 12345
print ("money = ", end=" ")
print(money, end=" ")
print(type(money))
if money is 12345:
    print ("money is 12345 (int)")
else:
    pass

print("\n")

money = "1"
print ("money = ", end=" ")
print(money, end=" ")
print(type(money))
if money == 1:
    print ("money = 1 (int)")
elif money == "1":
    print ("money = '1' (str)")
else:
    print ("none")

print("\n")

money = 1000000
print ("money = ", end=" ")
print(money, end=" ")
print(type(money))
# compare operator : > < >= <= == !=
if money > 10000:
    print ("money > 10000")
# and or not
if money > 10000 and money < 10e8:
    print ("10e4 < money < 10e8")

print("\n")

str_a = "python is easy...?"
print ("str_a = ", end=" ")
print(str_a, end=" ")
print(type(str_a))
if "python" in str_a:
    print ("python is in str_a")
if "cpp" not in str_a:
    print ("cpp is not in str_a")

print("\n")

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.\n")

num = 0
while num < 10:
    num = num +1
    if num % 2 == 0:
        continue
    print("num : %d" % (num))

print("\n")

coffee = 10
money = 300
# 무한 루프?
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.\n")
        break


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark < 60: continue
    print("%d번 학생 %d 점으로 축하합니다. 합격입니다. " % (number, mark))

print("\n")

for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 %d 점으로 축하합니다. 합격입니다." % (number+1, marks[number]))

print("\n")

for number, element in enumerate(marks):
    if element < 60: continue
    print("%d번 학생 %d 점으로 축하합니다. 합격입니다." % (number+1, element))

print("\n")

'''
money =  1 <class 'int'>
money == 1 (int)
money is 1 (int)


money =  12345 <class 'int'>
money is 12345 (int)


money =  1 <class 'str'>
money = '1' (str)


money =  1000000 <class 'int'>
money > 10000
10e4 < money < 10e8


str_a =  python is easy...? <class 'str'>
python is in str_a
cpp is not in str_a


나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.

num : 1
num : 3
num : 5
num : 7
num : 9


돈을 받았으니 커피를 줍니다.
남은 커피의 양은 9개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 8개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 7개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 6개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 5개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 4개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 3개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 2개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 1개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 0개입니다.
커피가 다 떨어졌습니다. 판매를 중지합니다.

1번 학생 90 점으로 축하합니다. 합격입니다.
3번 학생 67 점으로 축하합니다. 합격입니다.
5번 학생 80 점으로 축하합니다. 합격입니다.


1번 학생 90 점으로 축하합니다. 합격입니다.
3번 학생 67 점으로 축하합니다. 합격입니다.
5번 학생 80 점으로 축하합니다. 합격입니다.


1번 학생 90 점으로 축하합니다. 합격입니다.
3번 학생 67 점으로 축하합니다. 합격입니다.
5번 학생 80 점으로 축하합니다. 합격입니다.

'''
