import re

def check():
    pattern = "\w*\d*\.\d*\w*\d*@gmail.[com|org|in]*"
    n=re.findall(pattern,text)
    if n==[]:
        return 0
    else:
        return 1
    


text = input("Enter email id:")
b=check()
f=open("content.py","r")
if b==1:
    print(f.read())
else:
    print("The email id is not valid")

