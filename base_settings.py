def get_proxies():
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
    return proxies

def get_headers():
    headers =  {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
            "Accept": "*/*",
            "content-type": "application/json",
            "x-metadata": "{\"client\":\"PWA\",\"optionalClient\":\"PWA\"}",
        }
    return headers