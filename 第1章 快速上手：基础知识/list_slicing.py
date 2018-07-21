# _*_ coding:utf-8
# 切片学习demo

number = [1,2,3,4,5,6,7,8,9,10]

print(number[3:6])

# 复制列表
print(number[::])

# 倒序列表
print(number[::-1])

# 步长为正，起点到终点，实际是上对列表[6,7,8,9,10]进行切片
print(number[5::2])

# 步长为负，终点到起点，实际上是对列表[10,9,8,7]
print(number[:5:-2])