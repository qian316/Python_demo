# _*_ coding:utf-8 _*_
# 查看Python解释器模中模块的位置
import  sys,pprint
pprint.pprint(sys.path)
import copy

# import module_dmeo
# a = module_dmeo
# print(a.hello())
from module_test import module_dmeo
# import module_test.module_dmeo
print(module_dmeo.hello())

# 模块位置和模块文档
print(copy.__file__)
print(copy.__doc__)