from urllib import request
from bs4 import BeautifulSoup  #Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库.
import time,re
import requests
"""爬虫：1爬文本关键思路
    1.构建URL请求体；
    2.request去请求响应结果得到页面JS体（用到python中自带的urllib的request，美化html的bs4）
    3.find_all 定位爬虫目标
    4.写入本地。with open(r'path','w')as file: file.write(findresponse)
"""

def demoPChong():
        url="https://www.jianshu.com"
        # 构造头文件，模拟浏览器访问
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        # 打开Url,获取HttpResponse返回对象并读取其ResposneBody
        """一定注意这里引用的是urllib的request。不是urllib3"""
        page = request.Request(url=url, headers=headers)
        page_info = request.urlopen(page).read().decode('utf-8')
        #print(page_info)为HTML格式的网页解析
        # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
        soup = BeautifulSoup(page_info, 'html.parser')
        # 以格式化的形式打印html
        #print(soup.prettify())
        # 查找所有a标签中class='title'的语句
        titles=soup.find_all('a','title')
        print(titles)
        # for title in titles:
        #     print(title.string)
        #     print(url + title.get('href'))
        # open()是读写文件的函数,with语句会自动close()已打开文件
        # with open(r"D:\pachong\a.txt", "w") as file:  # 在磁盘以只写的方式打开/创建一个名为 articles 的txt文件
        #     for title in titles:
        #         file.write(title.string)
        #         file.write(url + title.get('href') + '\n\n')


def demoPcImg():
    url = "https://www.zhihu.com/question/22918070"
    h =request.urlopen()
    html = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    # 用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句
    links = soup.find_all('img', "origin_image zh-lightbox-thumb", src=re.compile(r'.jpg$'))
    print(links)

    # 设置保存图片的路径，否则会保存到程序当前路径
    path = r'D:\pachong\images'  # 路径前的r是保持字符串原始值的意思，就是说不对其中的符号进行转义
    for link in links:
        print(link.attrs['src'])
        # 保存链接并命名，time.time()返回当前时间戳防止命名冲突
        request.urlretrieve(link.attrs['src'], path + '\%s.jpg' % time.time())  # 使用request.urlretrieve直接将所有远程链接数据下载到本地

def demoPP():
    url="http://www.biqukan.com/1_1094/5403177.html"
    page = requests.get(url=url)
    page_info=page.text
    soup=BeautifulSoup(page_info)


demoPP()
