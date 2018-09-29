# _*_ coding:utf-8 _*_
# 构造函数__init__
class FooBar:
    def __init__(self):
        self.somevar = 42

f = FooBar()
print(f.somevar)

# 继承时候对构造函数的处理方法
## 第一种是调用未关联的超类构造函数
# class Brid:
#     def __init__(self):
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print('Aaaah...')
#             self.hungry = False
#         else:
#             print('No,Thanks!')
#
# class SongBride(Brid):
#     def __init__(self):
#         Brid.__init__(self)
#         self.sound = 'Squawk!'
#     def sing(self):
#         print(self.sound)
#
# sb = SongBride()
# print(sb.sing())
# print(sb.eat())
# print(sb.eat())

## 第二种使用函数super()
class Brid:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No,Thanks!')

class SongBride(Brid):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

sb = SongBride()
print(sb.sing())
print(sb.eat())
print(sb.eat())