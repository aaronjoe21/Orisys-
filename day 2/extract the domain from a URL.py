import re
URL=input("Enter the URL:")
domain= "https?:\/\/"
n=re.findall(domain,URL)
if n!=[]:
    domain= "www.\w+.\w+"
    n=re.findall(domain,URL)
    print(n)
else:
    print("NO DOMAIN")