import re
text=input("Enter a text:")
IP="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
da=re.findall(IP,text)
if da==[]:
    print("NOT A VALID IPV4")
else:
    print(da)

