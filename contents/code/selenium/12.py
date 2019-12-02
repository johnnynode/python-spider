from selenium import webdriver
import time

#创建浏览器对象
driver = webdriver.Chrome()
#加载请求指定url地址
driver.get("https://www.baidu.com")
#使用JavaScript开启一个新的选型卡
driver.execute_script('window.open()')
print(driver.window_handles)
#切换到第二个选项卡，并打开url地址
driver.switch_to_window(driver.window_handles[1])
driver.get("https://www.taobao.com")
time.sleep(2)
#切换到第一个选项卡，并打开url地址
driver.switch_to_window(driver.window_handles[0])
driver.get("https://www.jd.com")
#driver.close()