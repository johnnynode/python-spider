from selenium import webdriver
from selenium.webdriver.common.by import By

#创建浏览器对象
driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()
driver.get("http://www.taobao.com")
#下面都是获取id属性值为q的节点对象
input = driver.find_element_by_id("q")
print(input)

input = driver.find_element_by_css_selector("#q")
print(input)

input = driver.find_element_by_xpath("//*[@id='q']")
print(input)

#效果同上
input = driver.find_element(By.ID,"q")
print(input)

#driver.close()