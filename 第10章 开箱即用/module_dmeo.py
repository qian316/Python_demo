# _*_ coding:utf-8 _*_
# 模块中的测试代码
def hello():
    print("Hello, world!")

def test():
    hello()

#使用__name__就可以判断是主程序调用test代码还是，模块被引用了。
#当程序被调用时，以下代码和测试代码不会执行
if __name__ == '__main__':
    test()


