from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#创建浏览器对象
driver = webdriver.Chrome()
#加载指定url地址
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(url)
# 切换Frame窗口    
driver.switch_to.frame('iframeResult')
#获取两个div节点对象
source = driver.find_element_by_css_selector("#draggable")
target = driver.find_element_by_css_selector("#droppable")
#创建一个动作链对象
actions = ActionChains(driver)
#将一个拖拽操作添加到动作链队列中
actions.drag_and_drop(source,target)
time.sleep(3)
#执行所有存储的操作（顺序被触发）
actions.perform()
#driver.close()