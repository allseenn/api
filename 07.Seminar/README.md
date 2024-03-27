# Selenium

## Пакет Wildberries

Python3 программа по загрузке информации о желаемых товарах с сайта wildberries.ru включает следующие компоненты:

Фреймворки
- selenium

Внешние библиотеки

- json
- time
- pymongo

Внутренние модули

- db
- selen
- scraper
- tokens

Основной стартовый модуль

- main.py

### main.py

[Основной скрипт](https://github.com/allseenn/api/blob/main/07.Seminar/main.py) служит для запуска программы
из консоли с помощью следующи команд из директории с main.py

```bash MacOS
python3 main.py
```

```pwsh Windows
python main.py
```

```bash Linux
chmod +x main.py
./main.py
```

Программа запросит от пользователя ввода слова, по которому осуществит поиск на товаров с возможностью пагинации, сохранив конечный результат в JSON-файл или в базу данных MongoDB.

Формат сохраняемых данных следующий:

- _id - Уникальный артикул товара
- name - Модель товара
- brand - Марка производителя
- price - Цена
- link - Ссылка на страницу с описанием
- photos - Ссылки на фотографии

Имя сохраненного файла будет в виде *товар.json*

Предусмотрено сохранение в базу данных MongoDB, если раскомментировать соответствующую строку в main.py

В процессе работы программы, будет выводится служебная информация в консоль:

```
Введите товар для поиска: Принтер
Page 1 total 105 goods was scraped
Page 2 total 210 goods was scraped
Page 3 total 315 goods was scraped
Page 4 total 420 goods was scraped
Page 5 total 525 goods was scraped
Page 6 total 630 goods was scraped
Page 7 total 735 goods was scraped
Page 8 total 840 goods was scraped
Page 9 total 945 goods was scraped
Page 10 total 1050 goods was scraped
Page 11 total 1155 goods was scraped
Время выполнения: 178.15322017669678 секунд
Всего найдено 1155 товаров
Сохранено в Принтер.json 495 уникальных товаров
```

Большинство ошибок обрабатывается исключениями, позволяя программе продолжать работу, но с выводом неполадки в консоль.

