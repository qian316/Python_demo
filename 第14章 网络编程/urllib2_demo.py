# _*_ coding:utf-8 _*_
from urllib.request import urlopen
import re
# 打开远程文件
webpage = urlopen('http://www.python.org')
text = webpage.read()
m = re.search(b'<a href="([^"]+)".*?>about</a>',text,re.IGNORECASE)
print(m.group(1))
