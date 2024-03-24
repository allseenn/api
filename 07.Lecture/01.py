from libs import *

options = Options()
options.headless = True
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://www.amazon.com/")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Laptops")
search_box.submit()
time.sleep(2)
answer = driver.title
print(answer)
assert "Laptops" in answer
driver.quit()

