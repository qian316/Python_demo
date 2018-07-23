# _*_ coding:utf-8

x = [1,1,1]
print(x)
x[1] = 2
print(x)

# 删除列表元素
y = [1,2,3,4]
print(y)
del y[2]
print(y)

# 切片替换
name = list('Perl')
print(name)
name[1:] = list('ython')
print(name)

# 切片添加和删除
numbers = [1,5]
print(numbers)
numbers[1:1] = [2,3,4]
print(numbers)
numbers[1:4] = []
print(numbers)

#修改列表之新增
lst = [1,2,3]
lst.append(4)
print(lst)
# lst.clear()
# print(lst)
lst[:] = []
print(lst)

# extend 修改原有的列表
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

# sort
x = [4,6,2,1,7,9]
x.sort()
print(x)
x.sort(reverse=True)
print(x)
x.sort(reverse=False)
print(x)