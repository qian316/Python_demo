# _*_ coding:utf-8 _*_
#dict_demo

# dict
items = [('name','Gumbyu'),('age',42)]
d = dict(items)
print(d)

print(len(d))
print(d['age'])
d['age']  = 55
print(d['age'])
del d['age']
print(d)
print('name' in d )

# 一个简单的数据库
people = {
    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23'
    },
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
    },
    'Cecil':{
        'phone':'3158',
        'addr':'Baz avenue 90'
    }

}

# 电话号码和地址的描述性标签
labels = {
    'phone': 'phnoe number',
    'addr': 'address'
}

name = input('Name: ')

# 要找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')

# 使用正确的键：
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# 当名字是字典包含的键时，才打印的信息
if name in people:
    print("{}'s {} is {}.".format(name, labels[key], people[name][key]))


