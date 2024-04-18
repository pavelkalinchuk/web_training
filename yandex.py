from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import json

result_file = 'results/yandex.json'
data = {}

i = input("Введите что надо найти: ")

wd = Chrome()
wd.fullscreen_window()
wd.get("http://yandex.ru")
# Ниже записываем в переменную 'original_handle' идентификатор текущей вкладки
original_handle = wd.current_window_handle

# Так как строка поиска находится во фрэйме, то первой строкой делаем переход в него
wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR,"iframe"))
wd.find_element(By.CSS_SELECTOR, 'form.arrow').click()
wd.find_element(By.CSS_SELECTOR, '.arrow__input').send_keys(i)
wd.find_element(By.XPATH, '//button[@type="submit"]').click()

# Учитывая то, что результат поиска выводится на новую вкладку, то делаем переход на эту вкладку
for window_handle in wd.window_handles:
        if window_handle != original_handle:
                wd.switch_to.window(window_handle)

hrefs = wd.find_elements(
        By.CSS_SELECTOR, 'a[accesskey]')

for elem in hrefs:
    head = elem.get_attribute('innerText')
    href = elem.get_attribute('href')
    data[head] = href
# print(data)
data_json = json.dumps(data, ensure_ascii=False, indent=4)
# print(data_json)
with open(result_file, "w+") as f:
    f.write(data_json)

wd.close()