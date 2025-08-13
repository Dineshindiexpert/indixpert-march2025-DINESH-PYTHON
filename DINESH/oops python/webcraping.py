from bs4 import BeautifulSoup
import requests

url="https://www.academy.indixpert.com/student-dashboard/learn-program#"
data=requests.get(url)
htmlcontent= data.content
# print(htmlcontent)
soup= BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify)
tittle=soup.tittle
# print(tittle)
anchors=soup.find_all('a')
all_links=set()
for link in anchors:
     if (link!='#'):
          link=link.get('href')
          all_links.add(link)
          print(all_links)
     elif (link==','):
          continue

# print(soup.find('p')['class'])
# print(soup.find_all("p",class_="lead"))

# print(soup.find('p').get_text())