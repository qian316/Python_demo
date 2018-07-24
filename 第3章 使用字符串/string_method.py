# _*_ coding:utf-8 _*_
# String方法示例
# center两端添加相同的字符串
# test = "The Middle by Jimmy Eat world".center(39)
# print(test)
#
# test = "The Middle by Jimmy Eat world".center(39, "*")
# print(test)

# find 查找
y = 'With a moo-moo here, and a moo-moo there'
print(y.find('he'))
title = "Monty Python's Flying Circus"
print(title.find('Monty'))
print(title.find('Python'))
print(title.find('test'))

# join
dirs = '','usr', 'bin','env'
sep = '/'
print(sep.join(dirs))


# lower
low =  'Trondheim Hammer Dance'
print(low.lower())

# relace
rel = 'This is a test'.replace('is', 'eez')
print(rel)
rels = ('This is a test','This is a tist')
print(rels[1].replace('is', 'eez'))
# print(rels)


# split
print(sep.join(dirs).split('/'))
spl ='/usr/bin/env'.split('/')
print(spl)