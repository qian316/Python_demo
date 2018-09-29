# _*_ coding:utf-8 _*_


# 异常
# raise引发异常语句
def ThorwErr():
    raise Exception("抛出一个异常")
# Exception: 抛出一个异常
# ThorwErr()

# 自定义异常
class TestException(Exception):
    pass

# 捕获异常try/except语句
# try:
#     x = int(input())
#     y = int(input())
#     print(x/y)
# except ZeroDivisionError:
#     print("The seconde number can't e zero!")


# 可用except子句捕获多种异常，可在一个元组中指定这些异常
# try:
#     x = int(input())
#     y = int(input())
#     print(x/y)
# except (ZeroDivisionError,TypeError,NameError):
#     print("Your numbers were bogus")

# # 打印异常消息
# try:
#     x = int(input())
#     y = int(input())
#     print(x/y)
# except Exception as e:
#     print(e)

# finally子句
# 打印异常消息
try:
    1/ 0
except Exception as e:
    print(e)
finally:
    print("Cleaning up.")