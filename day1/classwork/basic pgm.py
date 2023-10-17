#1
'''
x=3
y=float('3.0')
z=int(y)
print(x+z)
'''

#2
'''
a=3
A=4
print(a+3+7)
'''

#3
'''
exp=3+True
print(exp)
'''

#4
'''
a35=6
32a=7
35_a=8
_a=9
a$=7
print(a$)
print(a35+35a)
print(35_a+_a)
'''


#5
def pgm1():
    a=input("Enter your name:")
    b=input("Enter age:")
    print("my name is",a,"and my age is",b)



#6
def pgm2():
    a=input("Enter your name:")
    b=input("Enter age:")
    if a=="ajay":
        print("my name is",a,"and my age is",b)
    else:
        print("Your name is invalid")


#7
def pgm3():
    name1=input("Enter the first name:")
    age1=int(input("Enter age:"))
    name2=input("Enter the second name:")
    age2=int(input("Enter age:"))
    if age1>age2:
        print("my name is",name1,"and my age is",age1)
    else:
        print("my name is",name2,"and my age is",age2)

pgm1()
pgm2()
pgm3()














