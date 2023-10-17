from bs4 import BeautifulSoup
import requests



file=open("index.html")
contents=file.read()
file.close()


#soup=BeautifulSoup(contents,"html.parser")
#print(soup.find_all(name='title'))
#print(soup.h1.text)
'''
print(soup.find(name="a").get("href"))
all_links=soup.find_all(name="a")
for link in all_links:
    print(link.getText)
    '''
'''
first_heading=soup.find(name="h1",id="first-heading")
print(first_heading.getText())
'''

'''
first_heading=soup.find(class_="small-para")
print(first_heading)
'''

response =requests.get("https://news.ycombination.com/")
print(response.txt)

S

#first_header=soup.select(selector=".last-para.headings")
#print("first_heading")

