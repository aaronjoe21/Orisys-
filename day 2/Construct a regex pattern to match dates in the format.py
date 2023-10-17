import re
text=input("Enter a text:")
date="\d\d\/\d\d\/\d\d\d\d"
date=re.findall(date,text)
print(date)