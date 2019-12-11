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
import requests
re=requests.get('https://news.baidu.com')
print(re.elapsed.total_seconds())