
# 基本数据类型（容器类型）
# 列表 list => [val1, val2, val3, val4]
# 元组 tuple => [val1, val2, val3, val4]
# 字典 dict => [key1:val1, key2:val2]
# 集合 set => [key, key, key, key]
# string 内置数据结构
# 数据结构

# ============================
# 列表 list
# ============================
# 处理一组有序项目的数据结构
# 列表时python中最灵活的有序集合对象类型·
# 列表可以包含任何的对象：字符串， 数字,甚至其他列表
# 列表是可变的数据类型，即使这种类型的值是可以被修改的
# 列表 = 链表 + 数组

# lst = []
# print(type(lst))
# """
# <class 'list'>
# """
# lst2 = list()
# print(lst2)
# """
# [] 空列表
# """
# lst3 = list('abc')  # list('iterable')
# print(lst3)
# """
# ['a', 'b', 'c']
# """
# print(list(range(3)))
# """
# [0, 1, 2]
# """

# ========================================
# 通过下标取值，与字符串相同
# lst = ['a', 1, 0.5, None, 'y']
# print(lst[4])
# '''
# y
# '''
# 列表可以包含任何的对象：字符串， 数字,甚至其他列表

# ========================================
# 列表是可变数据类型（在原来的内存地址修改值）
# 字符串不可变，只能重新赋值

# lst = ['a', 1, 0.5, None, 'y']
# print(id(lst))
# lst[1] = 2
# print(id(lst))
# print(lst)
# '''
# 2715147171392
# 2715147171392
# ['a', 2, 0.5, None, 'y']
# '''

# =========================================
# 列表的基本操作，增，删，改，查
# =========================================

# =========================================
# 增

# lst.append() # 追加一个元素，放在末尾

# 增加 lst.insert() # 在指定下标位置添加元素
# lst.insert(1, 'yy') # 在下标一处添加'yy'

# 增加 lst.extend('qwe') # 将'qwe'拆分增加到lst后面'q', 'w', 'e'
# 参数需要传入可迭代对象

# 列表可以进行加法运算和乘法运算[1, 2] + [3, 4] = [4, 6]
# [1, 2]*3 = [1, 2, 1, 2, 1, 2]

#=========================================
# 删

# lst = ['a', 'b', 'c']
# lst.pop()           # 返回值为最后一位（默认）
# print(lst)
# """
# ['a', 'b']
# """
# lst1 = ['a', 'b', 'c', '', 'y']
# lst.pop(2)           # 指定下标删除

# 指定下标删除，默认删除最后一位，返回删除对象

# 一条船，30个人
# 30个人进行编号，从1开始，数到第七个下船，最后输出下船的人
# member = list(range(1, 31))
# out = 6
# for i in range(4):
#     if out <= len(member)-1:
#         print(member.pop(out))
#         out += 6
#     else:
#         out = out - len(member)

# member = list(range(1, 31))
# while len(member) > 16:
#     i = 1
#     while i < 7:
#         member.append(member.pop(0))
#         i += 1
#         print(member.pop(0))
#

# remove 指定元素删除，无返回值
# lst.remove('') 删除列表中第一个匹配元素

# del ---- 删除 -----删除引用
# 只要能切片，就能删除
# del lst[::2]

# clear 清除列表
# lst.clear --->lst = []


# ===================================
# 修改
# lst = ['f', 'af', 'aa', '6']
# lst[3] = 'tt'
# lst[1:1] = 'qw'
# print(lst)
# lst[1:4] = 'ab'
# print(lst)
# lst[4:2] = 'rrr' # 结束切片为空为空，从开始的位置插入
# print(lst)

# lst.sort() lst.sort(reverse=True) # 顺序排序与逆序排序
# ord() # 查看ASCII

# ===================================
# 统计类
# len(lst) 长度 lst.count('') 元素出现次数 lst.index('')  下标位置

# 遍历
# =================================
# lst = ['aa', 'dd', 'ad']
# for i in lst:
#     print(i)
# for i in enumerate(lst):  # 按元组取出
#     print(i)
# for i,j in enumerate(lst):
#     print(f'{i}----{j}')

# 成员关系
# print('a' in lst)  --> ture or false

# 列表[1, 6, 8, 5, 4, 9, 7]
# 从键盘接受用户的输入， 输入一个整数
# 返回哪两个数相加等于所输入的整数，返回下标
# lst = [1, 6, 8, 5, 4, 9, 7]
# integer = int(input("请输入一个整数:"))
# for i, j in enumerate(lst):
#     for k, m in enumerate(lst):
#        if j + m == integer and i != k:
#          print(f'{j}+{m}={integer}')
#        break
#
# else:
#     print('ending...')