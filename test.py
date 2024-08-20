import requests
import json

# Define the request session
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "authority": "snapp.express",
    "method": "POST",
    "path": "/supermarket/%D8%A7%D8%B3%D9%85%D8%A7%D8%B1%D8%AA-%DB%8C%D9%88%D8%B3%D9%81-%D8%A2%D8%A8%D8%A7%D8%AF-(%D8%B3%D9%88%D9%BE%D8%B1%D9%85%D8%A7%D8%B1%DA%A9%D8%AA-%D8%B2%D9%86%D8%AC%DB%8C%D8%B1%D9%87-%D8%A7%DB%8C-%D8%A7%D8%B3%D9%86%D9%BE)%2B/api",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.6",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdLCJreWMiOjAsInVzZXJDb2RlIjpudWxsLCJzdWJzaWR5IjowLCJ1ZGlkIjoiMzQ4NDIzOTgtNzhlYi00ZjEwLWEzYWUtYWQ0MDRjYzM4YTQ4IiwiYXVkIjoic25hcHBmb29kX3B3YSIsImV4cCI6MTcyNDM5ODUyMywibmJmIjoxNzI0MTM5MjAzLCJpYXQiOjE3MjQxMzkyMDMsImp0aSI6ImY1MTdiZWQyLWZkOGYtNDVkOC1hZTk3LTI2ODhkMjIzNDY5YSIsInN1YiI6IiJ9.W7k_xqTsbL-5G8v0M77-Cpfu-I-cWJ7BerSKI7hFgNfW5EGkuIAAyiBbqcXAn85SqWvrJdojtmEfvl8FIpzUF1f5PmUNauUB-H-x_HQB3oKzIBnPXMZp8wEhLti5DimF38wHMXkMBY5dNc46anReo6BR2lTS1RYEp6ek-8OBUNoZHOlHgPXOJCvFZsay-nBD4nw5GdxtoWNm9miYqy0MO3pSuy6f_mo25s3IYh5iAjjPJo25-rw5WBLD3Vl-rzHAqw2dkconPlfhFo4L36BMNxO_BaNNJARA32jyY_hyBQm7FX967nRkFIwAIn6nDVQTpMwTl40Ve1T9rO7gv8yhyw",
    "origin": "https://snapp.express",
    "priority": "u=1, i",
    "referer": "https://snapp.express/supermarket/%D8%A7%D8%B3%D9%85%D8%A7%D8%B1%D8%AA-%DB%8C%D9%88%D8%B3%D9%81-%D8%A2%D8%A8%D8%A7%D8%AF-(%D8%B3%D9%88%D9%BE%D8%B1%D9%85%D8%A7%D8%B1%DA%A9%D8%AA-%D8%B2%D9%86%D8%AC%DB%8C%D8%B1%D9%87-%D8%A7%DB%8C-%D8%A7%D8%B3%D9%86%D9%BE)%2B/0yjd7m",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "traceparent": "00-1b5e5fffe7a496071dbad9b64d3cbfe7-f547dbf14b0d852d-01",
    "x-metadata": '{"client":"PWA","optionalClient":"PWA","deviceType":"PWA","appVersion":"5.6.6","clientVersion":"a4547bd9","optionalVersion":"5.6.6","UDID":"34842398-78eb-4f10-a3ae-ad404cc38a48","lat":"35.727","long":"51.393"}'
})

# Define the request body
request_body = {
    "operationName": "getSuperMarketProductList",
    "variables": {
        "variable": 1172,
        "secondVariable": "0yjd7m",
        'page':5,
        'pageSize':10
    },
    "query": """
        query getSuperMarketProductList($variable: Int, $secondVariable: String, $page: Int, $pageSize: Int) {
            superMarketProductList(
                variable: $variable
                secondVariable: $secondVariable
                page: $page
                pageSize: $pageSize
            ) {
                status
                data {
                    id
                    title
                    count
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
                                sectionNameFa
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
                        id
                        type
                        data {
                            id
                            title
                            score
                            rating
                            type
                            discount
                            discountRatio
                            description
                            price
                            vendorLogo
                            highlight
                            popularityBadgeUrl
                            commentCount
                            isEcommerce
                            noStock
                            brand
                            menuCategoryId
                            stock
                            capacity
                            images {
                                thumb
                                __typename
                            }
                            vendor {
                                title
                                code
                                vendorCode
                                category
                                rating
                                highlight
                                description
                                commentCount
                                address
                                vendorType
                                isOpen
                                isPreorderEnabled
                                isExpress
                                deliveryFee
                                deliveryTime
                                featured
                                minOrder
                                hasCoupon
                                couponCount
                                deliver
                                bestCoupon
                                paymentTypes
                                __typename
                            }
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
                __typename
            }
        }
    """
}

# Send the request
response = session.post("https://snapp.express/supermarket/%D8%A7%D8%B3%D9%85%D8%A7%D8%B1%D8%AA-%DB%8C%D9%88%D8%B3%D9%81-%D8%A2%D8%A8%D8%A7%D8%AF-(%D8%B3%D9%88%D9%BE%D8%B1%D9%85%D8%A7%D8%B1%DA%A9%D8%AA-%D8%B2%D9%86%D8%AC%DB%8C%D8%B1%D9%87-%D8%A7%DB%8C-%D8%A7%D8%B3%D9%86%D9%BE)%2B/api", json=request_body)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # print(json.dumps(data, indent=2))
    print(len(data['data']['superMarketProductList']['data']['finalResult']))
else:
    print(f"Request failed with status code {response.status_code}")