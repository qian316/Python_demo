# _*_ coding:utf-8 _*_
# 可以通过继承内置函数，来对内置函数进行派生
# 对list继承，一个带访问计数器的列表

class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.count = 0
    def __getitem__(self, index):
        self.count += 1
        return super(CounterList,self).__getitem__(index)

cl = CounterList(range(10))
print(cl)
cl.reverse()
print(cl.count)
cl[1] + cl[4]
print(cl.count)
