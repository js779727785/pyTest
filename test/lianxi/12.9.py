import requests
import json
dic={
    "aa":"valueA",
    "bb":True
}
"""
encode:
json=json.dumps(dic)
decode:
dic=response.json()
"""
"""
url_info='https://azure-sso.dianfubao.com/ssologin/client?client_id=clientIdForP2P&redirect_url=https://azure-www.qingyidai.com/src/tpl/proxyp.html'
s=requests.session()
re=s.get(url_info,allow_redirects=True,verify=False)
print(re.headers)
print(re.headers['Location'])
"""
#https 请求requests报错时
"""
1.python3报错的话，加上这两行代码就行了
#导入urllib3包
import urllib3
#使用这个方法就OK了
urllib3.disable_warnings()
"""
#接口文件的上传与下载
"""
# file = {
#    "files[]": ("1.png", open("d:\\1.png", "rb"), "image/png"),
#     "labels[]": "tu1",
#     }

#-------------多个文件用list类型------------
file = [
    ("files[]", ("1.png", open("d:\\1.png", "rb"), "image/png")),
    ("labels[]", "tu1"),
    ("files[]", ("2.png", open("d:\\2.png", "rb"), "image/png")),
    ("labels[]", "tu2"),
    ]
r = s.post(url1, data=f, files=file)
print r.content

#下载demo:https://www.cnblogs.com/Zhang-engineer/p/11392714.html
url = 'https://jypt.zhaotx.cn/upload/download/82F2413B8C13473AAECA512AA05124EA'
        r = ztx.session.get(url=url,stream=True,verify=False)#以流的形式进行下载文件
        if r.status_code ==200:#请求响应结果如果为200，将下载内容写入指定文件中
            with open(r'C:\\Users\Administrator\Desktop\11.doc','wb') as f:
                for chunk in r.iter_content(chunk_size=1024):#循环写入，chunk_size是文件大小
                    f.write(chunk)
"""
#MultipartEncoder用法:https://www.cnblogs.com/yoyoketang/p/8024039.html
"""
from requests_toolbelt import MultipartEncoder
"""
#获取响应时间，elapsed
"""
https://www.cnblogs.com/yoyoketang/p/8035428.html
r=requests.get('https://news.baidu.com')
try:
    r = requests.get("http://cn.python-requests.org/zh_CN/latest/",timeout=1)
    print(r.status_code)
    print(r.elapsed.total_seconds())
    print(r.elapsed.microseconds)
except:
    print("超过设置的timeout时间，以下microseconds超过1S时不能用，只显示小数位毫秒")
    print(r.elapsed.microseconds)
"""