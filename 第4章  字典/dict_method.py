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