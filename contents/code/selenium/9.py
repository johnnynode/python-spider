from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#创建浏览器对象
driver = webdriver.Chrome()
#加载请求指定url地址
driver.get("https://www.zhihu.com/explore")
#显式等待,最长10秒
wait = WebDriverWait(driver,10)
#等待条件：10秒内必须有个id属性值为zu-top-add-question的节点加载出来，否则抛异常。
input = wait.until(EC.presence_of_element_located((By.ID,'Popover1-toggle')))
print(input) #获取节点间内容
#driver.close()