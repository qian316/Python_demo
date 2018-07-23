# _*_ coding:utf-8

# permissions = 'rw'
#
# # 模糊查询
# print('w' in permissions)
# print('x' in permissions)
#
# users = ['mlh','foo','bar']
# print(input('Enter your user name: ') in users)
#
# # 对象中的子串
# subject = '$$$ Get rich now!!! $$$'
# print('$$$ ' in subject)

# demo,检查用户名和PIN码
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input('User name: ')
pin = input('PIN code: ')

if [username, pin] in database:
    print('Access granted')

