#!/usr/bin/env python3
import time
from wildberries.selen import *
def goods(keyword: str) -> list:
    driver.get("https://www.wildberries.ru/")
    time.sleep(4)
    #wait = WebDriverWait(driver, 5)
    # wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
    input = driver.find_element(By.ID, "searchInput")
    input.send_keys(keyword)
    input.send_keys(Keys.ENTER)
    page = 1
    cards_list = []
    cards = []
    while True:
        try:
            wait = WebDriverWait(driver, 5)
            cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@id]")))  
        except Exception as e:
            print(e)
        while True:
            driver.execute_script("window.scrollBy(0, 800)")
            try:
                wait = WebDriverWait(driver, 5)
                cards = cards + wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@id]")))
            except Exception as e:
                print(e)
            if len(cards) < 1:
                break
            elif len(cards) < 3:
                continue
            elif len(cards) > 100:
                driver.execute_script("window.scrollBy(0, -500)")
                break
        if len(cards) < 1:
            break

        for card in cards:
            card_dict = {}
            try:
                id = card.get_attribute("id")
                card_dict["_id"] = id
            except Exception as e:
                print(e)
                continue
            try:
                link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
            except Exception as e:
                print(e)
                link = None
            card_dict["link"] = link
            try:
                price = card.find_element(By.XPATH,  './/ins[contains(@class, "price__lower-price")]').text
                price = int(price.replace(" ", "").replace("₽", "").replace("&nbsp", "."))
            except Exception as e:
                print(e)
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
            except Exception as e:
                print(e)
                name = None
            cards_list.append(card_dict)
        
        print(f"Page {page} total {len(cards_list)} goods was scraped")
        try:
            driver.find_element(By.CLASS_NAME, "pagination-next").click()
        except:
            print(f"Обход всех страниц с товаром {keyword} закончен")
            break
        try:
            if driver.find_element(By.XPATH, '//span[@data-link="html{>xData.nocorrection? xData.userSearch:xData.search}"]'):
                print("label: NOTFOUND exists")
                break
        except:
            page += 1

    driver.quit()
    return cards_list

if __name__ == "__main__":

    print(goods("смартфон"))
