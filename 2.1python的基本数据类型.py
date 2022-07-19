# ===========================
#          整 型
# ===========================
# python2 中有整型与长整型之分 python3 中没有
# int 23
# loog 777777777777777777777777777

# 进制表示
# 二进制,以0b开头，进制转换函数bin(),接受一个int返回str
# a = 0b11
# print(a)
# b = 10
# result = bin(b)
# print(result)
# type(result) # class 'str'

# 八进制，以0o开头，进制转换函数oct()
#  a = 0o11
#  type(a)

# 十六进制以0x开头，进制转换函数hex(),接受一个int返回str

# int() 转换为十进制
# int('0x11', base=16)

# ============================================
# 加法计算全器
# 接受用户从键盘的输入
# 打印两数的和
# a = input("请输入加数：")
# b = input('请输入被加数：')
# c = a + b
# print(a, '+', b, '=', c, sep='')

# ============================================
# 进制转换器
# 输入任意10进制数
# 输出对应的二进制，八进制，十六进制数
# a = int(input('请输入一个数:'))
# b = bin(a)
# c = oct(a)
# d = hex(a)
#
# print(a, '的二进制数为:', bin(a))
# print(a, '的八进制数为:', c)
# print(a, '的十六进制数为:', d)


# =============================================
#               浮点型
# =============================================

# float 不精确，无限接近  二进制表示小数，有些数无法表示
# print(1 - 0.1)
# print(0.8 - 0.1)
# # 小数点后显示16位数
#
# from decimal import  Decimal       #从decimal导入Decimial模块
# my = Decimal.from_float(12.22)
# print(my)
# mydec = Decimal('12.22')
# print(mydec)

# =============================================
#                复数
# =============================================
a = 4 + 5j
print(type(a))
print(a.real, a.imag)   # 两者存储为浮点型


