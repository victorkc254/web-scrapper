from numpy import product
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

products =[]
for x in range(1,20):
    url='https://laptops/page-2/,'
    r = requests.get(url +str(x))
    soup= BeautifulSoup(r.content, 'html.parser')
    content= soup.find_all('div', class_="ut2-gl__body")
    
    for list in content:
        title = list.find('a', class_="product-title").text.replace('\n', ' ')
        price = list.find('span', class_="ty-price-num").text.replace('\n', ' ')
        price_tax= list.find('span', class_="ty-list-price ty-nowrap").text.replace('\n', ' ')
        
        info = [title, price, price_tax]
        
        products.append(info)
    print('Proucts Found:' ,len(products))
    time.sleep(3)
df = pd.DataFrame(products)
print(df.head())
df.to_csv('products.csv')
