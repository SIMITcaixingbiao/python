# 把函数作为参数传入

# map 映射
# ===========================
# 求取列表中每个元素的平方值
# lst = [1, 2, 3, 4, 5]
# lst2 = [3, 6, 7]
# def func(item):
#     return item*item
# result = map(func, lst)
# print(list(result))     # 可迭代对象转换
# result1 = map(lambda x:x**2, lst)
# print(list(result1))
# print(list(map(lambda x, y:x+y, lst, lst2)))

# 练习
# ==========================
# 有列表[1, 2, 3, 4, 5], 将所有元素转换成str:['1', '2', '3', '4', '5']
# 有列表字符串'span', 将个字符串转换成对应的sacii码的列表[115,112,97,109]
# 有列表[-1,-2,0,1,2], 将个元素转换为绝对值
# lst = [1, 2, 3, 4, 5]
# print(list(map(lambda x: str(x), lst)))
# print(list(map(lambda x: abs(x), [-1, -2, 0, 1, 2])))
# print(list(map(lambda x: ord(x), 'span')))

# filter 过滤 返回值为真，保留，为假，去除
# 取十以内的奇数
# result = filter(lambda x: x % 2, range(10))
# print(list(result))

# 1-200以内开平方是整数的数
# 过滤出100-999以内的水仙花数（153=1的立方+5的立方+3的立方）
# 把一个序列的空字符串去掉
# result = filter(lambda x: (x**0.5)%1==0, range(200))
# print(list(result))
# def f(x):
#     return x == ((x % 10) ** 3 + (x % 100 // 10) ** 3 + (x // 100) ** 3)
# print(list(filter(f, range(100, 1000))))

# sorted（） 排序
#=============================
# lst = [-6, 3, 2, -9, 7]
# lst2 = lst.copy
# lst.sort()
# print(lst, lst2)
# print(sorted(lst, key=abs)) #key指定排序方式

# 列表里包元组的形式排序
# lst = [(True, True, False),
#        (2, 1, 3),
#        (2, 2, 4),
#        (False, False, 3),
#        (False, False,2)]
# print(sorted(lst))

# 列表中的值忽略大小写排序
# 转换为小写，再排序，指针排序，值排序
# lst = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(lst, key=lambda x: x.lower()))
# d1 = {'a':3, 'b':2, 'c':1, 'd':4}
# print(sorted(d1, key=lambda x:d1[x]))

# ==========================
# reduce 累计（累加，累乘...）

# from functools import reduce
# a = [1, 2, 3, 4]
# def func1(x, y):
#     return x * 10 + y
# print(reduce(func1, a))

# lst = ['a', '1', 'bb', '234', '', '9']
# 使用reduce，取出lst里的数字，转化成整型，排序列出

#
