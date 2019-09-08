'''
1. 模拟登陆人人网
2. 登陆成功后跳转到个人首页并获取数据
'''

# 模拟人人网登陆操作
from urllib import request, parse

# 经过浏览器分析，页面上提交地址为：http://www.renren.com/PLogin.do
# 真正提交地址为：
login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201980202238"

# 经过浏览器xhr请求分析，真正的提交参数为：
# 不确定哪些是必须提交的数据，可以模拟浏览器所有数据均提交
data = {
    'email': '15311111111', # 此处为你的手机号
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': 1,
    'captcha_type': 'web_login',
    'password': '4566d0f4a94fyyz4f940abcd23f6a48f62589726a63106a2d7112ce194113cd1', # 此处是页面脚本加密后的密码
    'rkey': '00b732e6c4b8d408b75655e15dd43a82',
    'f': 'http%3A%2F%2Fwww.renren.com%2F111111111%2Fnewsfeed%2Fphoto'
}

data = parse.urlencode(data)

headers = {
    'Content-Length': len(data)
}

req = request.Request(login_url, data=bytes(data, encoding="utf-8"), headers=headers)
res = request.urlopen(req)

print(res.read().decode('utf-8')) # {"code":true,"homeUrl":"http://www.renren.com/home"} 此处表示登陆成功，将要跳转