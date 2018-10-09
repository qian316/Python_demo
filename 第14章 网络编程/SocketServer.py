# _*_ coding:utf-8 _*_
from socketserver import TCPServer,StreamRequestHandler

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting'.encode())

server = TCPServer(('',8888),Handler)
server.serve_forever()