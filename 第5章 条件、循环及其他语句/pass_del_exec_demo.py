# _*_ coding:utf-8 _*_
#pass_del_exec

#pass
name = 'Enid'
if name == 'Ralph Auldus Melish':
    print('Welcom!')
elif name == 'Enid':
    # 还未完成
    pass
elif name == 'Bill Gates':
    print('Access Denied')

# exec
from math import sqrt
scope ={}
exec('sqrt = 1', scope)
print(sqrt(4))
print(scope['sqrt'])

# eval
print(eval(input("Enter an arithmetic expression: ")))