# _*_ coding:utf-8 _*_
# 文件的基本方法

# read(n)
f = open(r'somefile.txt')
print(f.read(7))
print(f.read(4))
f.close()

# read()
f = open(r'somefile.txt')
print(f.read())
f.close()

# readline()
f = open(r'somefile.txt')
for i in range(3):
    print(str(i) + ': ' + f.readline(),end='')
f.close()

# readines()
import pprint
pprint.pprint(open(r'somefile.txt').readlines())
