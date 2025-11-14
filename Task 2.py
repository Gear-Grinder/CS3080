#Task 2
import requests
from bs4 import BeautifulSoup
url = 'https://openaccess.thecvf.com/CVPR2022?day=all'
web1 = requests.get(url)
soup = BeautifulSoup(web1.content, "html.parser")
inputs = soup.find_all('input')
author_dict = {}
for item in soup.find_all('input'):
    author = item.get('value')
    if author in author_dict:
        count = author_dict.get(author)
        author_dict[author] = count+1
    else:
        author_dict[author] = 1
max = 0
max_id = ""
for author, count in author_dict.items():
    if count > max:
        max_id = author
        max = count
print(max_id)