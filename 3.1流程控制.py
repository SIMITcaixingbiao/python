# 顺序结构
# 选择结构
# 循环结构
# ======================
# 顺序结构
# ======================
# import math
# a = int(input("请输入边长a："))
# b = int(input("请输入边长b："))
# c = int(input("请输入边长c:"))
# p = (a + b + c)/2
# s = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(f"三角形的面积为：{s}")

# ==========================
# if else 选择语句，分支结构 elif
# ==========================

# ==========================
# for 循环
#============================

# for item in interable:  interable 可迭代对象
#     do something
# else:
#     do somethong
# item -> 一个临时变量，用到接收当前循环的元素
# else -> 当for是正常退出时会执行else部分的代码

# num = 1
# for i in '新年快乐':
#     print(f"第{num}个字符为：{i}") # f使{}内转义
#     if num == 5:
#         break
#     num += 1
# else:
#     print('循环正常退出')
# print('end...')
#
# break 结束循环  continue 结束本次循环，开启下一次循环

# ======================================
# 让用户输入一个字符串
# 分别取出每个字符，如果为大写输出1，如果为小写输出零
# str1 = input('请输入一串字符串:')
# for i in str1:
#     if(ord(i) > 96):  # ord() chr()
#         print(0, end ='')
#     else:
#         print(1, end = '')

# ======================================
# range()  左闭右开
# for i in range(3):  # 顺序生成0-2
#     print(i)
# print(range(4, 9))

# range(start, end, step)

# =======================================
# 用户登录验证
# 登录成功/失败都给与提示
# 最多可尝试3次
# str1 = '123456'
# num = 2
# for i in range(3):
#     str2 = input('请输入密码：')
#     if str1 != str2:
#         print(f'密码错误，还剩{num}次机会')
#         num = num - 1
#         continue
#
#
#     else:
#         print('密码正确，登录成功')
#         break
# else:
#     print('机会用完')

# ========================================
# 猜数字
# 在程序内定义一个数字让用户猜
# 检查用户输入的是否是数字
# 键盘接受用户输入，猜对猜错都给出提示（大/小）
# 最多能猜三次
# 给出用户最终猜的结果，及花了几次猜



# =======================================
# while循环
# =======================================
# 只要condition的布尔值为True， 则一直循环
# while condition:
#     do something
# else: 循环正常退出时运行
#     do something

# =======================================
# 求取1到10的和
# count = 1
# s = 0
# while count < 11:
#     s += count
#     count += 1
# print(f'1-10的和为{s}')

# =======================================
# 千分位格式化
# num = input('请输入一串数字：')
# count = 0
# result = ''
# if num.isdigit():
#     for i in num[::-1]:
#         count += 1
#         result = i + result
#         if count % 3 == 0 and count !=len(num):
#             result = ',' + result
#     else:
#         print('千分位格式为：', result)
# else:
#     print('请输入数字')

# num[start:end:step] 字符串







