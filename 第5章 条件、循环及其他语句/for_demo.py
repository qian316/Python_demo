# _*_ coding:utf-8 _*_
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

# range
range(0,10)
print(list(range(0,10)))

# 打印1~100：
for number in range(1,101):
    print(number)

# 迭代字典，使用序列解包的形式返回键值对
d = {'x': '1','y': '2','z': '3'}
for key,value in d.items():
    print(key, 'corresponds to', value)