# _*_ coding:utf-8 _*_
import socket
s = socket.socket()

host = socket.gethostname()
port = 8888
s.bind((host,port))
# 最多允许多少个客户端连接
s.listen(5)
while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    # 发送数据
    # c.send('Thank you for connecting')
    c.send('Thank you for connecting'.encode())
    c.close()

