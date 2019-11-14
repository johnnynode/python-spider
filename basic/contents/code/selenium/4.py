from selenium import webdriver
import time

#创建浏览器对象
driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()
driver.get("http://www.taobao.com")
#下面都是获取id属性值为q的节点对象
input = driver.find_element_by_id("q")
#模拟键盘输入iphone
input.send_keys('iphone')
time.sleep(3)
#清空输入框
input.clear()
#模拟键盘输入iPad
input.send_keys('iPad')
#获取搜索按钮节点
botton = driver.find_element_by_class_name("btn-search")
#触发点击动作
botton.click()

#driver.close()