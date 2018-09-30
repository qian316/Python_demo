# _*_ coding:utf-8 _*_
# property特性
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    size =  property(get_size,set_size)

r = Rectangle()
r.size = 150 ,100
print(r.width)