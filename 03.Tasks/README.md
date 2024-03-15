# Сбор и разметка данных (семинары)

## Урок 3. MongoDB и Кликхаус

### Домашнее задание

1. Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе. https://www.mongodb.com/ https://www.mongodb.com/products/compass
2. Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.
3. Поэкспериментируйте с различными методами запросов.
4. Зарегистрируйтесь в ClickHouse.
5. Загрузите данные в ClickHouse и создайте таблицу для их хранения.


### Решение

1. [Написал подробную инструкцию](https://github.com/allseenn/api/blob/main/03.Lecture/README.md#mongodb) получения бесплатных аккаунтов Atlas MongoDB в условиях нынешней реальности.

2. [Загрузка списка литературы в MongoDB](https://github.com/allseenn/api/blob/main/03.Tasks/02.py)

3. [Скрипт с методами запросов](https://github.com/allseenn/api/blob/main/03.Tasks/03.py) выводит следующую информацию:

- Число книг в базе
- Список полей в документах
- Самая дешевая книга
- Самая дорогая книга
- Больше всего книг в наличие

4. [Написал подробную инструкцию](https://github.com/allseenn/api/blob/main/03.Lecture/README.md#clickhouse) по регистрации облачного ClickHouse при наших реалиях.

5. Загрузка данных в ClickHouse:

- [Скрипт c построчной обработкой](https://github.com/allseenn/api/blob/main/03.Tasks/04.py) загружает данные за 337.74 секунды на облачный сервис ClickHouse
- [Скрипт со списком кортежей](https://github.com/allseenn/api/blob/main/03.Tasks/05.py) загружает данные за 2.43 секунды на облачный сервис ClickHouse
