import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    button = browser.find_element_by_tag_name('button')
    button.click()
    # confirm = browser.switch_to.alert
    # confirm.accept()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    el_1 = browser.find_element_by_css_selector('#answer')
    el_1.send_keys(y)
    button = browser.find_element_by_tag_name('button')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
