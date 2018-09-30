# _*_ coding:utf-8 _*_
# sys.argv函数是传递给Python解释器参数的，索引0为脚本名
# 在终端中输入参数反转
import sys
args = sys.argv[1:]
args.reverse()
print(" ".join(args))