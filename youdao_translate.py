import random
from urllib import request, parse
import json

# 不断爬取翻译页面的功能，直到满足isOut为True
while True:
    key = input('请输入需要翻译的文字，输入exit表示退出：')
    if key == 'exit':  # 程序的出口
        break

    # 做真正的查询操作（此入口链接为特别弄的）
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    # 构造headers
    ua_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
               'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
               'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
               'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
               'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
               'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
               ]
    # 随机选择一个user—agent
    ua = random.choice(ua_list)
    headers = {
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    # 把form数据规范化
    formdata = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1523933959290",
        "sign": "248f5d216c45a64c38a3dccac0f4600d",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    # 对传递给服务端的数据，需要先做一次urlencode，保证浏览器能够识别
    data = bytes(parse.urlencode(formdata), encoding='utf-8')
    # 给服务器发送post请求
    req = request.Request(url, data, headers, method='POST')  # 比get多了data、method这两个参数
    response = request.urlopen(req)
    # 不解码会乱码 -> {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":1,"translateResult":[[{"src":"hello","tgt":"\xe4\xbd\xa0\xe5\xa5\xbd"}]]}\n'
    # 解码后 -> {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":1,"translateResult":[[{"src":"hello","tgt":"你好"}]]}
    info = response.read().decode('utf-8')  # info 为json的正则的字符串
    # print(info)
    # 将json转换成字典的格式
    jsonLoads = json.loads(info)
    print(jsonLoads['translateResult'][0][0]['tgt'])
