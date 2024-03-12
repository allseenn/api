# Сбор и разметка данных (семинары)

## Урок 2. Парсинг HTML. BeautifulSoup

Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех категориях: название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

Затем сохранить эту информацию в JSON-файле.

## Решение

[Данный скрипт](https://github.com/allseenn/api/blob/main/02.Tasks/01.py) осуществляет поиск книг на странице, при нахождении блока с литературой, скрипт сохраняет ее название в виде строки и цену в вещественном типе данных, далее переходит по ссылке, указанной в ее заголовке и копирует количество доступных экземпляров в целочисленном формате, а также сохраняет раздел с описанием как строку. После обработки, страницы целиком, происходит переход на следующую по порядку.
Информируя, пользователя о ходе выполнения парсинга в консоль:

```
Обрабатываем страницу № 9, прошло 27.98 секунд
```

Процесс обработки всех книг, в зависимости от скорости соединения, занимает несколько минут.
По завершении скрапинга всего каталога, выводится общее время выполнения скрипта, количество сохраненных книг и имя json-файла.

```
Обработано за 154.58 секунд 1000 книг, сохранено в books.json
```

JSON-файл имеет следующую структуру:

- name: string
- price: float
- availability: string
- available:integer
- description: string

<img src=pics/01.png>