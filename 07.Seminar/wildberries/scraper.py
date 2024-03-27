#!/usr/bin/env python3
from wildberries.selen import *
import time
def goods(keyword: str) -> list:
    driver.get("https://www.wildberries.ru/")

    input = driver.find_element(By.ID, "searchInput")
    time.sleep(3)
    keyword = "смартфон"
    input.send_keys(keyword)
    input.send_keys(Keys.ENTER)

    page = 1
    cards_list = []
    while True:
        time.sleep(3)
        try:
            wait = WebDriverWait(driver, 10)
            cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@id]")))  
        except Exception as e:
            print(e)
        while True:
            driver.execute_script("window.scrollBy(0, 800)")
            time.sleep(3)
            try:
                wait = WebDriverWait(driver, 10)
                cards = cards + wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@id]")))
            except Exception as e:
                print(e)
            if len(cards) < 30:
                break
            elif len(cards) > 99:
                driver.execute_script("window.scrollBy(0, -500)")
                break
        if len(cards) < 3:
            break

        for card in cards:
            card_dict = {}
            try:
                id = card.get_attribute("id")
                card_dict["_id"] = id
            except:
                continue
            try:
                link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                link = None
            card_dict["link"] = link
            try:
                price = card.find_element(By.XPATH,  './/ins[contains(@class, "price__lower-price")]').text
                price = int(price.replace(" ", "").replace("₽", "").replace("&nbsp", "."))
            except:
                price = None
            card_dict["price"] = price
            try:
                brand = card.find_element(By.CLASS_NAME, "product-card__brand").text
                card_dict["brand"] = brand
            except Exception as e:
                print(e)
            try:
                name = card.find_element(By.CLASS_NAME, "product-card__name").text
                name = name.replace("/ ", "")
                card_dict["name"] = name
            except:
                name = None
            cards_list.append(card_dict)
        
        print(f"Page {page} total {len(cards_list)} goods was scraped")
        driver.find_element(By.CLASS_NAME, "pagination-next").click()
        try:
            if driver.find_element(By.XPATH, '//h1[@class="not-found-search__title"]'):
                break
        except:
            page += 1
        if len(cards) < 3:
            break

    driver.quit()
    return cards_list

if __name__ == "__main__":

    print(goods("смартфон"))
