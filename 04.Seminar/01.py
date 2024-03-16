import requests
from lxml import html
import fake_useragent as ua
from pprint import pprint

headers = {'User-Agent': ua.UserAgent().random}

url = 'https://www.ebay.com/'
path = 'b/Apple-Laptops/111422/'
page = 'bn_320025'

requests = requests.get(url+path+page, headers=headers)

dom = html.fromstring(requests.text)
items_list = []
items = dom.xpath('//ul[@class="b-list__items_nofooter"]/li')
for item in items:
    item_info = {}
    name = item.xpath('.//h3[@class="s-item__title"]/text()')
    link = item.xpath('.//h3[@class="s-item__title"]/../@href')
    price = item.xpath('.//span[@class="s-item__price"]//text()')
    add_info = item.xpath('.//span[@class="NEGATIVE"]/text()')
    item_info['name'] = name
    item_info['link'] = link
    item_info['price'] = price
    item_info['add_info'] = add_info

    items_list.append(item_info)

pprint(items_list)