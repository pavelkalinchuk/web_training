from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import json

wd = Chrome(executable_path='/Users/pavelkalincuk/git/help_soft/chromedriver')
wd.implicitly_wait(30)
wd.get("http://yandex.ru")

data = {}

try:
    wd.find_element(By.XPATH, '//*[@id="text"]').click()
    wd.find_element(By.XPATH, '//*[@id="text"]').clear()
    wd.find_element(By.XPATH, '//*[@id="text"]').send_keys("test")
    wd.find_element(By.XPATH, '//button[@type="submit"]').click()
    hrefs = wd.find_elements(By.XPATH, "//li[@class='serp-item desktop-card']//a[@accesskey]")
    for elem in hrefs:
        data[elem.text] = elem.get_attribute('href')
    time.sleep(3)
    data_json = json.dumps(data, ensure_ascii = False, indent = 4)
    #print(data_json)
    with open("save.json", "w") as f:
        f.write(data_json)
finally:
    wd.close()

