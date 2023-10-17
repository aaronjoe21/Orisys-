from bs4 import BeautifulSoup
import requests

res=requests.get("https://news.ycombinator.com/")
content=res.text
a = BeautifulSoup(content,"html.parser")
print(a.title)

print("Headings:")
headings = a.find_all(name="span",class_ = "titleline") 
for heading in headings:
    print(heading.getText())

print("sscore:")
s = a.find_all(name="span",class_ = "score")
for score in s:
    print(score.getText())
print("Links in headings:")
links = a.find_all(name="span",class_ = "titleline")
for link in links:
    print(link.a.get("href"))