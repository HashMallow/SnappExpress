import pandas as pd
from Parallel import AsyncPool
from base_settings import *
from bs4 import BeautifulSoup
import asyncio
import aiohttp

proxies = get_proxies()
headers = get_headers()

async def link_generator(title, code):
    title = title.replace(' ', '-')
    url = f'https://snapp.express/supermarket/{title}+/{code}'
    return url

async def scrape(session, item):
    title, code = item
    url = await link_generator(title, code)
    try:
        async with session.get(url, proxy=proxies.get('http'), headers=headers) as res:
            print(url, res.status)
            # If you need to parse the content:
            # content = await res.text()
            # soup = BeautifulSoup(content, 'html.parser')
            # print(soup.prettify())
            # with open(f'{code}.html', 'w', encoding='utf-8') as file:
            #     file.write(str(soup))
            return url, res.status
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return url, str(e)

async def main():
    urls = []
    vendors_df = pd.read_csv("Vendors.csv")
    for title, code in zip(vendors_df['title'], vendors_df['code']):
        urls.append((title,code))
    
    async with aiohttp.ClientSession() as session:
        pool = AsyncPool(100)
        results = await pool.map(lambda item: scrape(session, item), urls)
    
    # Process results if needed
    for result in results:
        if result:
            url, status = result
            print(f"Processed {url} with status {status}")

if __name__ == "__main__":
    asyncio.run(main())