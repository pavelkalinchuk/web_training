from selenium import webdriver
import time

wd = webdriver.Chrome(executable_path='/Users/pavelkalincuk/git/help_soft/chromedriver')
wd.implicitly_wait(30)
wd.get("http://yandex.ru")
time.sleep(3)
wd.close()
