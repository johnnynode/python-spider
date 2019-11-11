from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
input = driver.find_element_by_id("kw")
input.send_keys('python')
input.send_keys(Keys.ENTER)

print(driver.page_source)

# driver.close()