from libs import *

time_start = time.time()
#driver.get("https://www.auchan.ru")
driver.get("https://www.wildberries.ru/")

input = driver.find_element(By.ID, "searchInput")
time.sleep(3)
keyword = "смартфон"
input.send_keys(keyword)
input.send_keys(Keys.ENTER)

while True:
    while True:
        wait = WebDriverWait(driver, 10)
        cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@id]")))
        count = len(cards)
        driver.execute_script("window.scrollBy(0, 1500)")
        # time.sleep(1)
        # cards = driver.find_elements(By.XPATH, "//article[@id]")
        time.sleep(1)
        wait = WebDriverWait(driver, 10)
        cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@id]")))
        if count == len(cards):
            break

    cards_list = []
    for card in cards:
        card_dict = {}
        article = card.get_attribute("id")
        card_dict["article"] = article
        link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
        card_dict["link"] = link
        price = card.find_element(By.CLASS_NAME, "price__lower-price").text
        card_dict["price"] = price
        brand = card.find_element(By.CLASS_NAME, "product-card__brand").text
        card_dict["brand"] = brand
        name = card.find_element(By.CLASS_NAME, "product-card__name").text
        card_dict["name"] = name
        cards_list.append(card_dict)

    driver.find_element(By.CLASS_NAME, "pagination-next").click()
    if driver.find_element(By.XPATH, '//h1[@class="not-found-search__title"]'):
        break



driver.quit()

with open("cards.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["article", "link", "price", "brand", "name"])
    for card in cards_list:
        writer.writerow([card["brand"], card["name"], card["price"], card["article"], card["link"]])

print(f"Найдено и сохранено {len(cards_list)} товаров в файл {keyword}.csv, за {time.time() - time_start:.2f} с")