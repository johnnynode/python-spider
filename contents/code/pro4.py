'''
模拟人人网登录和获取个人主页数据的整个过程
通过cookie管理器，用于状态维持和会话跟踪技术
'''

# 模拟人人网登陆操作
import requests
import gzip
import re,time

ses = requests.Session() # 获取可以维持会话状态的请求对象

# 登录函数
def doLogin():
    login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201980202238"
    data = {
        'email': '15311111111',
        'icode': '',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': 1,
        'captcha_type': 'web_login',
        'password': '4566d0f4a94fyyz4f940abcd23f6a48f62589726a63106a2d7112ce194113cd1',
        'rkey': '00b732e6c4b8d408b75655e15dd43a82',
        'f': 'http%3A%2F%2Fwww.renren.com%2F111111111%2Fnewsfeed%2Fphoto'
    }
    ses.post(login_url, data=data)
    print('登录成功!')

# 获取个人数据
def getData():
    # 请求示例：http://www.renren.com/111111111
    req_url = "http://www.renren.com/your-id"
    res = ses.get(req_url)
    html = res.content.decode('utf-8')
    print(re.findall(("<title>(.*?)</title>"), html)) # ['人人网 - 你的名字'] 此处会输出如下信息

if __name__ == "__main__":
    # 登录
    print("登录中...")
    doLogin() # 登录操作
    # 此处用于模拟，应该在回调中实现获取个人数据
    time.sleep(2) # 此处仅作模拟, 延迟2s的时间
    getData() # 获取个人数据