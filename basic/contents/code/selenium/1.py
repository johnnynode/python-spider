from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() # 获取谷歌浏览器driver实例对象
driver.get('http://www.baidu.com') # 打开百度
input = driver.find_element_by_id("kw") # 找到页面上id为kw的元素
input.send_keys('python') # 在里面输入 关键词 python
input.send_keys(Keys.ENTER) # 在输入框中执行回车操作

print(driver.page_source) # 打印页面资源内容

# driver.close()