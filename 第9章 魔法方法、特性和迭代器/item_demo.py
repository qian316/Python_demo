# _*_ coding:utf-8 _*_

# 自己通过元素访问来建立一个算术序列

def check_index(key):
    """
    指定的键是否是可接受的索引？

    键必须是非负整数，才可以接受。如果不是整数，
    将引发TypeError异常；如果是负数，将引发IndexError异常(因为这个序列的长度是无穷的)
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise  IndexError

class ArithmeticSequence:
    def __init__(self, start = 0, step =1):
        """
        初始化这个算术序列
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        从算术序列中获取一个整数
        """
        check_index(key)
        try:
            return  self.changed[key]
        except KeyError:
            return  self.start + key * self.step

        def __setitem__(self, key, value):
            """
            修改算术序列中的元素
            """
            check_index(key)

            self.changed[key] = value

s = ArithmeticSequence(1,2)
# start = 1 ,step = 2, key= 4
# start + key * step
print(s[4])
print(s[5])
