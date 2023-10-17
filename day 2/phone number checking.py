import re
sum=0


phone=input("Enter phone number:")
pattern = "\(\d{3}\).\d{3}-\d{4}"
n=re.findall(pattern,phone)
if n==[]:
    print("Phone number is invalid")


pattern="\d"
n=re.findall(pattern,phone)
b=len(n)
if b==10:
    print("Phone number is valid")
elif b<10:
    print("Phone number is invalid")
else:
    pattern="\+\d+"
    n=re.findall(pattern,phone)
    if n!=[]:
        print("The phone number is valid")
    else:
        print("Invalid")