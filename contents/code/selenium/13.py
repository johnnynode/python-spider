from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#创建浏览器对象
driver = webdriver.Chrome()
try:
    #加载请求指定url地址
    driver.get("https://www.baidu.com")
except TimeoutException:
    print('Time Out')

try:
    #加载请求指定url地址
    driver.find_element_by_id("demo")
except NoSuchElementException:
    print('No Element')
finally:
    #driver.close()
    pass
