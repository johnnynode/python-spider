from selenium import webdriver

#创建浏览器对象
driver = webdriver.Chrome()
#使用隐式等待(固定时间)
driver.implicitly_wait(2) 
#加载请求指定url地址
driver.get("https://www.zhihu.com/explore")
#获取节点    
input = driver.find_element_by_id("Popover1-toggle")
print(input) #获取节点间内容

#driver.close()