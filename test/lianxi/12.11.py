__author__ = "Jmelody"
"""一个简单的selenium启动
from airtest.core.api import *
from airtest_selenium.proxy import WebChrome
from lib.log import logger
chrome_driver='C:/Program Files (x86)/Google/Chrome/Application/chromedriver_78.exe'
driver = WebChrome(executable_path=chrome_driver)
driver.implicitly_wait(20)

url='https:/news.baidu.com'
driver.get(url)
time.sleep(3)
cookies=driver.get_cookies()
logger.info("driver.cookies:"+str(cookies))
driver.quit()
"""
#获取响应内容结构，并爬取
"""
re=requests.get('https://news.baidu.com')
from bs4 import BeautifulSoup
soup=BeautifulSoup(re.content,"html.parser")
titles=soup.find_all(class_='xx')
print(titles)
"""
#下载url图片并保存到本地，打开
"""
import requests
res = requests.get('https://res.pandateacher.com/xx.png')
#发出请求，并把返回的结果放在变量res中
pic=res.content
#把Reponse对象的内容以二进制数据的形式返回
photo = open(r'c:/Users/Administrator/Desktop/ppt.jpg','wb')
#新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
#图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
photo.write(pic)
#获取pic的二进制内容
photo.close()
#关闭文件
#打开图片：
from PIL import Image
im = Image.open(r'C:\\Users\Administrator\Desktop\logo.png')
im.show()
"""
import requests,poco
re=requests.get('https://news.baidu.com')
from bs4 import BeautifulSoup
soup=BeautifulSoup(re.content,"html.parser")
print(soup)
