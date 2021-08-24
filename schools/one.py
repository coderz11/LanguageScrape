from bs4 import BeautifulSoup
import requests

url = 'https://www.icls.com.my/'
response = requests.get(url)
print(response)

html = response.content
soup = BeautifulSoup(html, 'html.parser')

all_h3 = soup.select('div.box-text-inner h3 a')
for h3 in all_h3:
    print(h3.get_text(strip=True))
