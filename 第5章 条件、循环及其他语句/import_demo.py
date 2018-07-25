# _*_ coding:utf-8 _*_
# import_demo
# 模块别名
# import math as foobar
# print(foobar.sqrt(4))
# 函数别名
from math import sqrt as foobar
print(foobar(4))

# 序列解包
x, y, z = 1, 2, 3
print(x, y, z)

x, y = y, x
print(x,y,z)

x, y, *s = 1, 2, 3, 4
print(s)

a, *b, c = "abc"
print(a, b, c)

# 链式赋值
value = 100
a = b = c = value
print(a,b,c,value)

