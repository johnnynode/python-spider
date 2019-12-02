from selenium import webdriver
from selenium.webdriver import ActionChains

#创建浏览器对象
driver = webdriver.Chrome()
#加载请求指定url地址
driver.get("https://www.zhihu.com/explore")
#获取id属性值为zh-top-link-logo的节点（logo）
logo = driver.find_element_by_id("zh-top-link-logo")
print(logo) #输出节点对象
print(logo.get_attribute('class')) #节点的class属性值
#获取id属性值为zu-top-add-question节点（提问按钮）
input = driver.find_element_by_id("zu-top-add-question")
print(input.text) #获取节点间内容
print(input.id)  #获取id属性值
print(input.location) #节点在页面中的相对位置
print(input.tag_name) #节点标签名称
print(input.size)     #获取节点的大小
#driver.close()