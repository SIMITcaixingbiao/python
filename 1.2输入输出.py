# =========================
#            输入
# =========================

# input() 接收用户从键盘的输入
# username = input("please input your name:")  # 里面为提示信息，将键盘输入赋值给username
# password = input("please input password:")
# print(username, type(username))
# print(password, type(int(password)))         # int 强制转换整型

# print('12' + '34')     # 字符串相加
# print(12 + 34)         # 整型相加

# =========================
#       隐藏输入
# =========================

# getpass
# import getpass                                         # 引入getpass模块
# username = input("please input your name:")
# password = getpass.getpass("please input password:")    # 使用getpass功能
# print('your name is:', username)
# print('your password is:', password)
# # vim python_test python3 python_test

# ===============================
# 1.输入年龄、姓名、爱好并输出
# 2.简易用户登录：输入用户名密码，并输出"XX,欢迎您"
# ===============================
# 1.
# name = input('请输入姓名:')
# age = input('请输入年龄:')
# hooby = input('请输入爱好:')
# print('name:', name)
# print('age:', age)
# print('hooby', hooby)

# 2.
# name = input('please input your name:')
# password = input('please input your password:')
# print(name+',欢迎您')

# =================================
#               输出
# =================================
# print(value, ...,sep=' ', end='\n', file=sys.stdout,flush=False)
# sep 分隔符； end 某位指定追加符号 默认换行；


# file 指定输出位置，默认输出到屏幕
# 还可以输出到文件
# 以读写的形式打开文件file.txt
# f = open("file,txt", 'w+')
# print('a', 'b', 'c', file=f)

# python之禅 import this

# 语法检测工具
# pip install flake8
# flake8 test_pass.py   检测语法

# a = input('please input a:')  # a = int(input('please input a:'))
# b = input('please input b:')
# print(a + b)
# print(int(a) + int(b))
# 转换为整型
