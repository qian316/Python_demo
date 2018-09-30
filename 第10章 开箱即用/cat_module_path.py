# _*_ coding:utf-8 _*_
# 查看Python解释器模中模块的位置
import  sys,pprint
pprint.pprint(sys.path)

# import module_dmeo
# a = module_dmeo
# print(a.hello())
from module_test import module_dmeo
# import module_test.module_dmeo
print(module_dmeo.hello())