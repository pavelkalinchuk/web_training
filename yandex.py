from selenium import webdriver
import time

wd = webdriver.Chrome(executable_path='/Users/pavelkalincuk/git/help_soft/chromedriver')
wd.implicitly_wait(30)
wd.get("http://yandex.ru")
wd.find_element_by_xpath('//*[@id="text"]').click()
wd.find_element_by_xpath('//*[@id="text"]').clear()
wd.find_element_by_xpath('//*[@id="text"]').send_keys("test")
wd.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
wd.close()
