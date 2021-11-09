from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

wd = Chrome(executable_path='/Users/pavelkalincuk/git/help_soft/chromedriver')
wd.implicitly_wait(30)
wd.get("http://yandex.ru")

try:
    wd.find_element(By.XPATH, '//*[@id="text"]').click()
    wd.find_element(By.XPATH, '//*[@id="text"]').clear()
    wd.find_element(By.XPATH, '//*[@id="text"]').send_keys("test")
    wd.find_element(By.XPATH, '//button[@type="submit"]').click()
    hrefs = wd.find_elements(By.XPATH, "//li[@class='serp-item desktop-card']//a[@accesskey]")
    for elem in hrefs:
        print (">> Text: " + elem.text + "\n    URL: " + elem.get_attribute('href'))
    #print(hrefs)
    time.sleep(3)
finally:
    wd.close()
