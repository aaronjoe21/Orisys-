import re
text=input("Enter a text:")
date="https?:\/\/\S+"
da=re.findall(date,text)
if da==[]:
    print("No URL")
else:
    print(da)
