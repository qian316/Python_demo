# _*_ coding:utf-8 _*_
# 递归的练习

## 阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))

# 二分查找
