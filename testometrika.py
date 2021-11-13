from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import json

wd = Chrome(executable_path='/Users/pavelkalincuk/git/help_soft/chromedriver')
wd.implicitly_wait(30)

#data = {}
with open("data.json", "r") as f:
    data = json.loads(f.read())

url = (data.get("url1"))
#start_test = (r'//div[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div/a/span[4]')
try:
    wd.get(url)
    wd.find_element(By.XPATH, '//div[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div/a/span[4]').click()
#    wd.find_element(By.XPATH, '//span[@class="text"]').text
#    wd.find_element(By.XPATH, '//*[@id="text"]').send_keys("test")
#    wd.find_element(By.XPATH, start_test).click()
#    hrefs = wd.find_elements(By.XPATH, "//li[@class='serp-item desktop-card']//a[@accesskey]")
#    for elem in hrefs:
#        data[elem.text] = elem.get_attribute('href')
    time.sleep(5)
#    data_json = json.dumps(data, ensure_ascii = False, indent = 4)
#    #print(data_json)
#    with open("save.json", "w") as f:
#        f.write(data_json)
finally:
    wd.close()

