# Сбор и разметка данных

## Урок 1. Парсинг API

### Домашнее задание

1. Ознакомиться с некоторые интересными API. https://docs.ozon.ru/api/seller/ https://developers.google.com/youtube/v3/getting-started https://spoonacular.com/food-api

2. Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.

3. Сценарий Foursquare

4. Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).

5. Используйте API Foursquare для поиска заведений в указанной категории.

6. Получите название заведения, его адрес и рейтинг для каждого из них.

7. Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

### Решение

#### Задача 1

Ознакомился:

<table>
<tr><td><img src=pics/01.png></td><td><img src=pics/02.png></td></tr>
<tr><td><img src=pics/03.png></td><td><img src=pics/04.png></td></tr>
</table>

#### Задача 2

Написал запросы, которые меня интересуют (бесплатны):

- [YouTube Data API v3](https://github.com/allseenn/api/blob/main/01.Tasks/01.py)

- [spoonacular API](https://github.com/allseenn/api/blob/main/01.Tasks/02.py)

<div style="page-break-before: always;"></div>

#### Задачи 3-7

Сценарий foursquare: 

1. запрашивает ввод категорий (слово, либо предложение) 

2. осуществляет поиск по категориям

3. выводит список ближайших мест по ip: Название, адрес

- [FourSquare API](https://github.com/allseenn/api/blob/main/01.Tasks/03.py)

### Вопросы

Перерыл все API FourSquare и не нашел, где рейтинг. Вся информация по рейтингам относится к api второй версии, который с 2022 года deprecated. Буду признателен за подсказку про API v3 для получения рейтингов.