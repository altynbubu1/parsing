from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.house.kg/kupit'

response = requests.get(URL)

soup = bs(response.content, 'html.parser')

publics = soup.findAll('div', class_='listing')

listing = []

for i in range(len(publics)):
    title = publics[i].find('p', class_='title').get_text(strip=True)
    address = publics[i].find('div', class_='address').get_text(strip=True)
    price_bax = publics[i].find('div', class_='price').get_text(strip=True)
    price_som = publics[i].find('div', class_='price-addition').get_text(strip=True)
    description = publics[i].find('div', class_='description').get_text(strip=True)

    images = publics[i].findAll('img')
    urls = [i.get('data-src') for i in images]

    result = {
        'title': title,
        'address': address,
        'price_bax': price_bax,
        'price_som': price_som,
        'description': description,
        'images': urls
    }

    listing.append(result)
    # print(listing)

# with open('lesson_1.json', 'w', encoding='utf-8') as file:
#     json.dump(listing, file, ensure_ascii=False, indent=4)
