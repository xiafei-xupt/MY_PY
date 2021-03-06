'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

'''
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
print(list(zipped))
# [(1, 4), (2, 5), (3, 6)]
b = zip(a,c)              # 元素个数与最短的列表一致
print(list(b))
# [(1, 4), (2, 5), (3, 6)]
