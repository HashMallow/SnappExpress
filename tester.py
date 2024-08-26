import requests
import pandas as pd
from Parallel import *
from base_settings import *
from bs4 import BeautifulSoup
from lxml import etree


urls = []
def link_generator(title, code):
    title = title.replace(' ', '-')
    url = f'https://snapp.express/supermarket/{title}+/{code}'
    return url

vendors_df = pd.read_csv("Vendors.csv")
proxies = get_proxies()
headers = get_headers()

def scrape(item):
    title, code = item
    url = link_generator(title, code)
    res = requests.get(url, proxies=proxies)
    # soup = BeautifulSoup(res .content, 'html.parser')
    # print(soup.prettify())
    # with open('output.html', 'w', encoding='utf-8') as file:
    #     file.write(str(soup))
    # if res.status_code != 200:
        print(url, res.status_code)

for title, code in zip(vendors_df['title'], vendors_df['code']):
    urls.append((title,code))
    break

pool = ThreadPool(40)
pool.map(scrape, urls)
pool.wait_completion()