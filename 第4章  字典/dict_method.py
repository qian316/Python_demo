# _*_ coding:utf-8 _*_

# clear
d = {}
d['name']  = 'Gumby'
d['age']  = 44
print(d)

returned_value = d.clear()
print(d)

# copy
x = {'username': 'admin', 'password': ['123','456']}
y = x.copy()
print(y)
y['username'] = 'root'
y['password'].remove('123')
print(x)
print(y)

# deepcopy
from copy import deepcopy
d = {}
d['name'] = ['admin','root']
c = d.copy()
dc  = deepcopy(d)
d['name'].append('_admin')
print(c)

print(dc)

# get
test_get = {}
print(test_get.get('name'))

print(test_get.get('name','N/A'))


# 一个简单的数据库，用get方法获取
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

# name = input('Name: ')

# 要找电话号码还是地址？
# request = input('Phone number (p) or address (a)? ')

# 使用正确的键：
# key = request
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'

# get提供默认值
# person = people.get(name,{})
# label = labels.get(key,key)
# result = person.get(key,'not avvilable')

# print("{}'s {} is {}.".format(name, label, result))

# items
items_test = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
items_test.items()
print(items_test)

# popitem
items_test.popitem()
print(items_test)

items_test['name'] = 'admin'
print(items_test)

# update
x = {'title': 'Python Lanuage Website','password':'123'}
items_test.update(x)
print(items_test)

# values
y = {}
y.values()
print(y)