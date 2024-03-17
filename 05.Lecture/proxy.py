import requests
import ping3
from fake_useragent import UserAgent as ua
#from tokens import ProxyScrapeApiKey

def proxy_list_from_file(file_name: str)->list:
    with open(file_name, 'r') as f:
        ROTATING_PROXY_LIST = f.read().splitlines()
    return ROTATING_PROXY_LIST

def fastest_proxy(proxy_list: list)-> str:
    """Проверяет скорость соединения с каждым прокси из proxy_list, 
        и возвращает самый быстрый в виде строки ip:port"""
    best_proxy_id = 0
    speed = 10000
    for id, proxy in enumerate(proxy_list):
        host, port = proxy.split(":")
        try:
            ping = ping3.ping(host, timeout=1)
        except ping3.exceptions.PingError:
            continue
    if ping < speed:
        speed = ping
        best_proxy_id = id

    return proxy_list[best_proxy_id]


def proxy_list_from_proxyscrape()->list:
    #https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
    proxy = "http://38.162.28.107:3128"
    url = "https://api.proxyscrape.com"
    path = "/v2"
    file = "/"
    params = {
        "anonymity": "all",
        "request": "getproxies",
        "protocol": "http",
        "timeout":10000,
        "country": "all",
        "ssl": "all"
    }
    headers = {
        "User-Agent": ua().random
    }

    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    response = session.get(url+path+file, params=params, headers=headers)

    return response.text.split()

def main(source: str)->str:
    if(source == "file"):
        proxy_list = proxy_list_from_file("proxy_list.txt")
    elif(source == "api"):
        proxy_list = proxy_list_from_proxyscrape()
    return fastest_proxy(proxy_list)



if __name__ == "__main__":
    print(main("api"))

