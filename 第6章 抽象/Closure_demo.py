# _*_ coding:utf-8 _*_
# 函数嵌套函数，multiplyByFactor这种存储其所在作用域的函数的方式叫做闭包
def multiplier(factor):
 def multiplyByFactor(number):
    return number * factor
 return multiplyByFactor


# 一开始并不清楚，调用外层函数的时候，是先给哪个参数传值，
# 后来打断点运行的时候，才知道先给外面函数参数赋值，然后在给里面函数的参数赋值。
double = multiplier(2)
print(double(5))


print(multiplier(5)(4))