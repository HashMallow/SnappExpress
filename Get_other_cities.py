import requests
import json
import argparse
import numpy as np
import time
from threading import Thread
from queue import Queue
import pandas as pd
import multiprocessing
import math


CPU_THREADS = multiprocessing.cpu_count() 
MAX_THREADS = CPU_THREADS * 4

class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:
    """ Pool of threads consuming tasks from a queue """

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()

# parser = argparse.ArgumentParser(description="SnappExpress Killer")
# parser.add_argument("-l", "--lat", type=float,default=32.68056, help="latitude")
# parser.add_argument("-t","--lon", type=float,default=51.65259, help = "longitude")
# parser.add_argument("-c","--city", type=str,default="Esfahan")


# args = parser.parse_args()

url = "https://snapp.express/vendor-list/api"


payload = {
    "operationName": "getVendorList",
    "variables": {
        "variable": "-1",
        "page": 0,
        "pageSize": 100,
        "filters": {
            "superType": [4],
            "mode": "CURRENT",
            "item_position": "homePage"
        }
    },
    "query": """
    query getVendorList($variable: String, $page: Int, $pageSize: Int, $filters: JSONObject) {
      vendorList(
        variable: $variable
        page: $page
        pageSize: $pageSize
        filters: $filters
      ) {
        status
        data {
          count
          openCount
          extraSections {
            filters {
              top {
                data {
                  title
                  value
                  __typename
                }
                __typename
              }
              sections {
                data {
                  title
                  value
                  __typename
                }
                __typename
              }
              __typename
            }
            __typename
          }
          finalResult {
            data {
              id
              title
              isMarketParty
              backgroundImage
              commentCount
              minimumOrderValue
              code
              status
              area
              countReview
              isExpressPin
              logo
              isOpen
              preOrderEnabled
              deliveryFee
              deliveryTime
              discountValueForView
              rating

              __typename
            }
            type
            __typename
          }
          __typename
        }
        __typename
      }
    }
    """
}

def is_in_circle(lat, lon):
    if math.sqrt(math.pow(lat-alat, 2) + math.pow(lon-alon, 2)) <= radius:
        return True
    return False

def scrape(item):
    global dicts, proxies
    i,lat,lon = item
    if not is_in_circle(lat, lon):
        return None
    print(i)
    headers = {
        "User-Agent": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "x-metadata": json.dumps({
            "client": "PWA",
            "optionalClient": "PWA",
            "lat": f"{lat}",
            "long": f"{lon}"
        }),
    }

    un = True
    while un:
        try:
            response = requests.post(url, headers=headers, json=payload,proxies=proxies)
            if response.status_code == 200:
                un=False
        except:
            pass
        time.sleep(0.5)


    # Check if the request was successful
    if response.status_code == 200:
        dicts[i] = []
        data = response.json()
        # Now you can work with the data
        for it in data['data']['vendorList']['data']['finalResult']:
            dicts[i].append(it)
            print(it['data']['title'])
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)




# Proxy information
proxy_domain = "p.webshare.io"
proxy_port = "80"
proxy_username = "velrbxxn-rotate"
proxy_password = "np1basaqv9ok"

# Construct the proxy URL
proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_domain}:{proxy_port}"

# Set up the proxy dictionary
proxies = {
    "http": proxy_url,
    "https": proxy_url
}
import os
if __name__ == '__main__':
    cities_df = pd.read_excel('cities.xlsx')
    for city, alat, alon in zip(cities_df['english_title'],cities_df['latitude'],cities_df['longitude']):
        flag = False
        for item in os.listdir('Data'):
            if item == f'Express_Vendors_{city}.csv':
                flag = True
                break
        if flag:
            continue
        print(city, end=":\n\n")
        radius = 0.12
        if city in ["Esfahan", "Tabriz", "Mashhad"]:
            radius = 0.17
        latitudes = np.linspace(alat - radius,alat + radius,80)
        longitudes = np.linspace(alon - radius,alon + radius,90)
        dicts = {}
        cnt = 1
        items = []
        for latitude in latitudes:
            for longitude in longitudes:
                items.append((cnt,latitude,longitude))
                cnt+=1
        pool = ThreadPool(MAX_THREADS)
        pool.map(scrape, items)
        pool.wait_completion()

        final_list = []
        for item in dicts:
            final_list += dicts[item]

        dk = {}
        for i in range(len(final_list)):
            dk[i] = final_list[i]['data']

        df = pd.DataFrame(dk).T
        df.drop(columns=['deliveryFee'], inplace = True)
        df.drop_duplicates(inplace=True)
        df.to_csv(f'Express_Vendors_{city}.csv', index=False, encoding='utf-8-sig')