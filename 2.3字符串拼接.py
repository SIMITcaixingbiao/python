# ===================================
# 字符串拼接
# ===================================
# 加号拼接
# str1 = 'i' + 'am' + 'lili'
# str2 = 'beatfullan'*3
# print(str1)
# print(str2)

# .join()拼接
# str3 = ''.join(['i', 'am', 'lili']) #列表，可迭代对象
# print(str3)

# 字符串格式化
# 使用百分号占位符%进行格式化
# %s 表示字符串
# %d 表示整形十进制 转换成整型输出
# %f 表示浮点数
# %x 表示十六进制
# %o 表示八进制
# name = 'cai'
# age = 18
# print('i am %s, my age is %s'%(name, age)) # name 填第一个% age填第二个%
# print('i am %s, my age is %d'%(name, age))
# print('i am %s, my age is %x'%(name, age))
# print('i am %s, my age is %o'%(name, age))

# 基本格式
# %[(name)][flags][width].[precision]typecode
# -(name):命名
# -flags：+,-,''或0.+表示正前面填充“+”；-表示左对齐
# ' '表示正数左侧填充一个空格，与负数对齐，0表示用0填充 对字符串无用
# -width 表示显示宽度
# -precision 表示小数点后精度
# print("第一个格式化：%010x" % 10)
# print("第二个格式化：%-11x" %10)
# print("第三个格式化：%+x" %10)

# print("第四个格式化：%010.3f" %2.1352314)
# print("第五个格式化：%.4f" %4.546577)
# print("第六个字符串：%s %%"%('sc'))  # 两个%%表示%本身
#
# f1 = 0.2344616
# # 转换为百分号表示，保留两位小数
# print("%.2f %%"%(100*f1))

# ===================================
#             format
# ===================================
# name = 'cai'
# age  = 18
# print("format01 --> 姓名：{}，年龄：{}".format(name, age))  # 按顺序填充
# print("format01 --> 姓名：{1}，年龄：{0}".format(name, age)) # 参数代表顺序数
# print("format01 --> 姓名：{x}，年龄：{y}".format(x = name, y = age)) # 指定字符串

# format 格式化
#{变量：[填充字符][对齐方式（^）[宽度][格式]]}
# print("format03 --> {0:*>8}".format(10,20))
# print("format04 --> {num:@^10}".format(num=35))
# print("format05 --> {1:*>15.2f}".format(1/3, 6.333333))
# print("format06 --> {0:x}".format(10))

# 千分位格式化
# print("format07 --> {0:,}".format(123456789))

# f 标志位 python3才有
# name = "cai"
# age = 18
# print(f"my name is {name:a^10}, my name is {age}")
 #===========
 # 练习
 # ==========
a = '字符串拼接1'
b = '字符串拼接2'
print(a + b)
print("".join([a, b]))
print("{}{}".format(a, b))
print("%s%s"%(a, b))
print(len(a + b))
print((a + b)[7:8:1])
# 请用四种以上的方式将a与b拼接成字符串c
# 请计算新拼接的字符串长度，并取出其中的第七个字符，
# 将字符串'8*y*cali*china**it*soft*linux*python'里所有的'*'号抽取出来放到最前面，
# 里面的字符串保持顺序不变
str1 = '8*y*cali*china**it*soft*linux*python'
str2 = str1.split('*')
str3 =''.join(str2)
print(str3)
str4 = str1.count('*')
str5 = str4*'*'
print(str3 + str5)