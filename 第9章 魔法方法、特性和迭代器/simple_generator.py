# _*_ coding:utf-8 _*_
# 简单生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1,2],[3,4],[5]]
for num in flatten(nested):
    print(num)

print(list(flatten(nested)))