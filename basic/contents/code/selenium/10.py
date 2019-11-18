from selenium import webdriver
import time

#创建浏览器对象
driver = webdriver.Chrome()
#加载请求指定url地址
driver.get("https://www.baidu.com")
driver.get("https://www.taobao.com")
driver.get("https://www.jd.com")
time.sleep(2)
driver.back() #后退
time.sleep(2) #前进
driver.forward()
#driver.close()