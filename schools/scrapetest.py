from django.db import models
from bs4 import BeautifulSoup
import requests

url = 'https://www.icls.com.my/'
response = requests.get(url)
print(response)

html = response.content
soup = BeautifulSoup(html, 'html.parser')

datas = []
all_h3 = soup.select('div.box-text-inner h3 a')
for h3 in all_h3:
    data = h3.get_text(strip=True)
    datas.append(data)
latestdatas = set(datas)
print(latestdatas)