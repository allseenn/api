from libs import *

driver.get("https://quotes.toscrape.com/page/1/")
# ожидание загрузки элемента
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".quote")))
# извлечение данных из элемента
quote = element.text
driver.quit()
print(quote)