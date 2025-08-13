from bs4 import BeautifulSoup
import requests

url = "https://www.youtube.com/@icscoachingcentreofficial"

data = requests.get(url)
html = data.content

soup = BeautifulSoup(html, 'html.parser')

# Use a set to store unique href values
# links = set()

# # Find all anchor tags
# for tag in soup.find_all('a', href=True):
#     href = tag['href']
#     # Filter out invalid or empty hrefs
#     if href != "#" and not href.startswith("javascript:"):
#         links.add(href)

# # Print all extracted links
# for link in links:
#     print(link)
PARAGRAPH=soup.find_all('href')
print(PARAGRAPH)
   
