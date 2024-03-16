import requests
import csv
from lxml import html
from pprint import pprint
from fake_useragent import UserAgent as ua
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.utf8')

#search_text = "+".join(input("Поиск по названию товара: ").split())
# https://gb.ru/topics - продолжение темы второго семинара задача 2
url = 'https://gb.ru'
file = '/topics'
headers = {'User-Agent': ua().random}

page = 1
params = {
    "page": page,
}
session = requests.Session()

items_list = []
while True:
    response = session.get(f"{url}{file}?page={page}", headers=headers)
    dom = html.fromstring(response.text)
    items = dom.xpath('//div[@class="topics-list__item topic-item"]')
    if not items:
        break

    for item in items:
        item_info = {}
        item_info['author'] = item.xpath('.//a[@class="topic-item-statistics__user-name"]/text()')[0]
        item_info['author_link'] = url+item.xpath('.//a[@class="topic-item-statistics__img-wrapper"]/@href')[0]
        try:
            item_info['count_answer'] = int(item.xpath('.//div[@class="topic-answers__counter topic-answers__counter_color_green"]/text()')[0])
        except:
            item_info['count_answer'] = 0
        item_info['last_answer'] = item.xpath('.//div[@class="topic-item-statistics__text topic-item-statistics__text_color_muted"]/text()')[0]
        item_info['tags'] = item.xpath('.//a[@class="topic-item__tag-link"]/text()')
        time_str = item.xpath('.//div[@class="topic-item__date"]/text()')[0].replace(' в ', ' ').strip().title()
        item_info['time'] = datetime.strptime(time_str, '%d %B %Y %H:%M').strftime('%Y-%m-%d %H:%M')
        item_info['topic'] = item.xpath('.//a[@class="topic-item__title"]/text()')[0]
        item_info['topic_link'] = url+item.xpath('.//a[@class="topic-item__title"]/@href')[0]
        items_list.append(item_info)
    print(f"Обработана страница № {page}")
    page += 1

with open('gb_topics.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=items_list[0].keys())
    writer.writeheader()
    writer.writerows(items_list)

