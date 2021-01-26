import csv
import requests
from bs4 import BeautifulSoup

args = []

for x in range(51):
    url = 'https://diskontshop.eu/category/BADY/Vitaminy/?page={}'.format(x)

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response = requests.get(url, headers=header)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    container = soup.select_one('ul.product-list')

    products = container.find_all('a')

    urls = []
    for product in products:
        path = product.get('href')
        if(path != '#' and path != '/cart/' and path != '/AP-05532173/' and path != '/AP-00789447/' and path != '/AP-11662164/' and path != '/AP-09239487/' and path != '/AP-06175798/' and path != '/AP-00379985/' 
        and path != '/AP-07115982/' and path != '/AP-09719201/' and path != '/AP-01079334/' and path != '/AP-02513620/' and path != '/AP-09201332/' and path != '/AP-08506621/' and path != '/AP-02695696/'):
            url = 'https://diskontshop.eu' + path
            urls.append(url)

    for url in urls:
            response = requests.get(url, headers=header)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            name = soup.find('span',{'itemprop':'name'}).text
            price = soup.select_one('span.price.nowrap').text
            for url in urls:
                path = soup.find('div', {'class':'image'}).find_next('img')['src']
                img = 'https://diskontshop.eu' + path
            description = soup.find('div', {'id':'product-description'}).text
            args.append((name, price, description, img, url))

    print('Status message: page = {}'.format(x))

names = ['Название', 'Цена', 'Описание', 'Картинка', 'Ссылка']


with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(names)

    for ar in args:
        writer.writerow(ar)

