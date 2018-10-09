# _*_ coding:utf-8 _*_
from urllib.request import urlopen
from urllib.request import urlretrieve
import re
# 打开远程文件
# webpage = urlopen('http://www.python.org')
# text = webpage.read()
# m = re.search(b'<a href="([^"]+)".*?>about</a>',text,re.IGNORECASE)
# print(m.group(1))

# 获取远程文件
## python官网无法打开，更换为百度网址
# a  =  urlretrieve('http://www.python.org','/python_webpage.html')
urlretrieve('http://www.baidu.com','C:\\Users\\qian\\Python_demo\\第14章 网络编程\\python_webpage.html')
