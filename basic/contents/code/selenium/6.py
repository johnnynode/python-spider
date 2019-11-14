from selenium import webdriver

#创建浏览器对象
driver = webdriver.Chrome()
#加载指定url地址
driver.get("https://www.zhihu.com/explore")
#执行javascript程序将页面滚动移至底部
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#执行javascript实现一个弹框操作
driver.execute_script('window.alert("Hello Selenium!")')

#driver.close()