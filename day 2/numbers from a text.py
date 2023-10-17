import re
number=input("Enter a message:")
pattern = "\d+"
n=re.findall(pattern,number)
print(n)

