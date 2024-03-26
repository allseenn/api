import time
import csv
from selenium import webdriver # Импорт основного драйвера
from selenium.webdriver.common.keys import Keys # Класс клавиш клавиатуры
from selenium.webdriver.common.by import By # Класс поиска с помощью чего..
from selenium.webdriver.firefox.options import Options # Класс опций передаваемых драйверу
from selenium.webdriver.support.ui import WebDriverWait # Класс ожидания
from selenium.webdriver.support import expected_conditions as EC # Класс ожидаемых события

options = Options()
options.headless = True
# options.add_argument("start-maximized")
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)