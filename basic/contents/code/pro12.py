import os,time
import requests
from urllib.parse import urlencode
from urllib.request import urlretrieve
import ssl

def getPage(offset):
    '''爬取指定url页面信息'''
    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': 0,
        'format': 'json',
        'keyword': '美食',
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': 1578116528279
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'referer': 'https://www.toutiao.com/',
        'cookie': 'csrftoken=66e3c07e4d9cc9a308ccb1748f143db0; tt_webid=6746722527713691150; Hm_lvt_668f5751b331d2a1eec31f2dc0253443=1578116375; tt_webid=6746722527713691150; s_v_web_id=56a2a67b21725d5cf98e1a52aff7114d; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=ezw3p7i181578116422980; Hm_lpvt_668f5751b331d2a1eec31f2dc0253443=1578116440'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def getImages(json):
    '''解析获取图片信息'''
    data = json.get('data')
    if data:
        for item in data:
            # print(item)
            display = item.get('display') # display 字段
            # 下面一系列字段初始化
            emphasized = None 
            title = None 
            selfInfo = None
            imageList = None 
            if display and type(display).__name__=='dict':
                emphasized = display.get('emphasized') # emphasized 字段
                if emphasized:
                    title = emphasized.get('title')
                selfInfo = display.get('self_info') # self_info 字段
                if selfInfo:
                    imageList = selfInfo.get('image_list') # image_list 字段
                    # print(imageList)
                    for image in imageList:
                        yield {
                            'image': image.get('url'),
                            'title': title
                        }

def saveImage(item):
    '''储存图片'''
    # 处理每组图片的存储路径
    title = item.get('title').replace('<em>', '').replace('</em>', '')
    path = os.path.join("./mypic/",item.get('title'))
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as e:
            print(e)

    # 拼装原图和目标图片的路径即名称
    image_url = item.get('image')
    image_url = image_url.replace('300x196','960x624') # 替换成大图
    save_pic = path + "/" + image_url.split("/").pop() + ".jpg"

    # 使用urllib中urlretrieve直接存储图片
    ssl._create_default_https_context = ssl._create_unverified_context
    urlretrieve(image_url, save_pic)

def main(offset):
    ''' 主程序函数，负责调度执行爬虫处理 '''
    json = getPage(offset)
    for item in getImages(json):
        # print(item)
        saveImage(item)

# 判断当前执行是否为主程序运行，并遍历调用主函数爬取数据
if __name__ == '__main__':
    # 此处试爬2页数据，(数据量太大)
    for i in range(2):
        main(offset=i*20)
        time.sleep(1)