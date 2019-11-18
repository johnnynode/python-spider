from selenium import webdriver
from selenium.webdriver import ActionChains

#创建浏览器对象
driver = webdriver.Chrome()
#加载请求指定url地址
driver.get("https://www.zhihu.com/explore")
print(driver.get_cookies())
driver.add_cookie({'name':'Joh','domain':'www.zhihu.com','value':'zhangsan'})
print(driver.get_cookies())
driver.delete_all_cookies()
print(driver.get_cookies())
#driver.close()