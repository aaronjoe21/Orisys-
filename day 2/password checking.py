import re

def check2(n,sum):
    if n==[]:
        return sum
    else:
        a=sum=sum+1
        return a
        


def check():
    sum=0
    pattern = "(?:[A-Z])"
    n=re.findall(pattern,text)
    sum=check2(n,sum)
    pattern = "(?:[0-9])"
    n=re.findall(pattern,text)
    sum=check2(n,sum)
    pattern="[A-Za-z\d]"
    n=re.findall(pattern,text)
    c=len(n)
    if c>=8:
        sum=sum+1
    return sum
text = input("Enter password:")
b=check()
f=open("content 2.py","r")
if b==3:
    print(f.read())
else:
    print("PASSWORD IS NOT STRONG")