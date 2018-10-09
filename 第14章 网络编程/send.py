# _*_ coding:utf-8 _*_
import socket
s = socket.socket()

host = socket.gethostname()
port = 8888
s.connect((host,port))
# 接收数据，并制定接收最多多少个字节的数据
print(s.recv(1024))

