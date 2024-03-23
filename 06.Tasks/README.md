# Урок 6. Scrapy.

## Парсинг фото и файлов

### Домашнее задание

1. Создайте новый проект Scrapy. Дайте ему подходящее имя и убедитесь, что ваше окружение правильно настроено для работы с проектом.
2. Создайте нового паука, способного перемещаться по сайту www.unsplash.com. Ваш паук должен уметь перемещаться по категориям фотографий и получать доступ к страницам отдельных фотографий.
3. Определите элемент (Item) в Scrapy, который будет представлять изображение. Ваш элемент должен включать такие детали, как URL изображения, название изображения и категорию, к которой оно принадлежит.
4. Используйте Scrapy ImagesPipeline для загрузки изображений. Обязательно установите параметр IMAGES_STORE в файле settings.py. Убедитесь, что ваш паук правильно выдает элементы изображений, которые может обработать ImagesPipeline.
5. Сохраните дополнительные сведения об изображениях (название, категория) в CSV-файле. Каждая строка должна соответствовать одному изображению и содержать URL изображения, локальный путь к файлу (после загрузки), название и категорию.

### Решение

Создаем директорию для выполенния 6 домшней работы:

```
mkdir 06.Tasks
```

Прямо в директории 6 домашки создаем проект Scrapy по имени splash:

```
scrapy startproject splash . # вместо папки указываем . (текущая диркетория), чтобы не плодить папки
```

Создаем паука по имен unsplash для домена  www.unsplash.com:

```
scrapy genspider unsplash www.unsplash.com
```

### Настройки (settings.py)

Указываем, тот браузер, с помощью которого исследуем целевой сайт, для правильного скренирования, иначу будут появлятся другие теги, либо атрибуты:

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

Количество одновременных подключений указываю 10, т.к. сайт proxyscrape.com на бесплатном тарифе выделяет 100 прокси, но 10 одновременных к ним подключениям, больше сессий ставить нет смысла:

CONCURRENT_REQUESTS = 10

Чтобы не палиться, отключаем прием печенек:

COOKIES_ENABLED = False

Включаем поддержку карусель прокси:

DOWNLOADER_MIDDLEWARES = {
   'rotating_proxies.middlewares.RotatingProxyMiddleware': 100,
   'rotating_proxies.middlewares.BanDetectionMiddleware': 110,
}

Указываем путь к списку прокси:

ROTATING_PROXY_LIST_PATH = '../../proxy_list.txt'

Включаем пайплайны, т.е. постобработку полученного контента:

ITEM_PIPELINES = {
   "splash.pipelines.SplashPipeline": 300, # обработчик по-умолчанию с приоритетом ниже чем для фото
   "splash.pipelines.PhotoPipeline": 200, # обработчик для фото
}

Обязательно указать место для сохранения скачанных фоток:

IMAGES_STORE = "photos"

### Отладочный файл runner.py
Импортируем класс управления сборщиком:

from scrapy.crawler import CrawlerProcess

Импортируем класс реактор сборщика:

from scrapy.utils.reactor import install_reactor

Импортируем класс для логирования
from scrapy.utils.log import configure_logging

Класс загрузки настроек из файла settings.py

from scrapy.utils.project import get_project_settings
from splash.spiders.unsplash import UnsplashSpider

Устанавливаем ту корневую директорию из которой запущен runner.py
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Стандартное условие выполениние следующего кода, если запущен сам файл runner.py
if __name__ == "__main__":
    настройки логирования
    configure_logging()
    включение асинхронного реактора для реализации многопоточности
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    настройка логирования
    configure_logging
    создание процесса сборщика с указанными настройками
    process = CrawlerProcess(get_project_settings())
    запрос к пользователя для ввода желаемой темы фоток для поиска
    #query = input("Введите тему для поиска: ")
    включение в процесс сборщика конкретного паука и конкретной темы для поиска
    process.crawl(UnsplashSpider, query='Python3')
    запуск на исполение процесса
    process.start()


Данный файл не нужен для штатной работы программы, но он нужен для отладки программы. Для запуска в режиме отладки открываем в VSC runner.py и запускаем деббагер.

### Настройка паука unsplash.py

В директории spiders у нас только один паук unsplash.py.

### Пайплайны pipelines.py

