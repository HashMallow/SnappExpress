import requests
import json

url = "https://snapp.express/vendor-list/api"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Accept": "*/*",
    "Content-Type": "application/json",
    "x-metadata": json.dumps({
        "client": "PWA",
        "optionalClient": "PWA",
        "lat": "35.69",
        "long": "51.401"
    }),

    # "Sec-Fetch-Mode": "cors",
}

payload = {
    "operationName": "getVendorList",
    "variables": {
        "variable": "-1",
        "page": 0,
        "pageSize": 18,
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

response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Now you can work with the data
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)