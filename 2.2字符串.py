# =========================
#      字符串的表示
# =========================

# a = 'hello'
# b = "world"
# c = ''' '''

# 字符串前置r
# a = 'hello \nworld'
# b = r'hello \n world'   # r 不转义，作为原始字符串输出
# print(a)
# print(b)

# 转义字符 \n \a:响铃

# 字符串切片
# str1 = "abcdefghijklm"
# print(str1[3])   # 顺序 3
# print(str1[-6])  # 逆序 6
# 通过下标去切片
# str[start:end:step]
# print(str1[3:7:2])  # 3-7 步长2 步长默认为1
# step 为正，表示顺序截取， 为负，逆序截取

# 字符串是不可变序列，不能修改，只能重新赋值，字符串相邻，自动级联

# =========================
#      字符串的常用方法
# =========================

# 判断
# =====================================================
# str.isdigit()               #字符串中是否只包含数字
# str.isnumeric()             #字符串中是否只包含数字（包括中文一到九等）
# str.isalnum()               #字符串中是否只包含字母或数字
# str.istitle()               #字符串中是否只有首字母大写，其他字母小写
# str.isalpha()               #字符串中是否只包含字母（汉字会算作字母）
# str.isupper()               #字符串中是否全为大写

# a = 'abxd'
# str1 = '1234567'
# str2 = '123一二三'
# str3 = 'abc123'
# str4 = 'hello sanchuang'
# print(str1.isnumeric())
# print(str2.isnumeric())
# print(str3.isnumeric())

# .startswith('') startswith('',7) 字符串第七个以  开始 ''对象，开始位，结束位
# .endswith(''，，)
# str1 = 'abcdefg xxxyyy'
# print(str1.startswith('abc'))
# print(str1.startswith('xx',8))
# print(str1.endswith('yy'))

# 查找统计类
# ================================================
# len(string)  统计字符串的长度
# str.count(sub[,start[,end]])  统计substring在字符串里出现的次数
# str.index(sub[,start[,end]])  显示substring在字符串中第一次出现的下标位置，没有会报错
# str.find(sub[,start[,end]])   查找substring，找到返回其起始位置，找不到返回-1
# print(len('dhzshd'))
# print(len('dhzshd三国杀'))
# print('aadsfasdfsdf'.count('a', 0))

# 转换类
# ================================
# msg.upper() 转为大写
# msg.lower() 转为小写
# msg.title() 首字母大写
# msg.swapcase() 大小写互换

# 切割
# ================================
# msg.split(":")   按冒号切割

# 拼接
# ================================
# .join()
# msg = "root:x:0:0root:/root"
# msg_list = msg.split(':')
# print(msg_list)
# print('#'.join(msg_list)) # 以井号键拼接

# msg = 'ab**5%ef'
# # 把星号和百分号替换成井号
# msg_list1 = msg.split('**')
# print('##'.join(msg_list1))
# msg_list2 = '##'.join(msg_list1)
# msg_list3 = msg_list2.split('%')
# print('#'.join(msg_list3))

# 替换
# ==================================
# msg.replace('', '')   后者替换前者 用空白替换即是删除
# msg = 'afa*ssf'
# print(msg.replace('*', '#'))

# 去除首尾字符（默认是空白字符）
# msg.strip()
# msg = ' afsfs'
# msg2 = '#sfsf#'
# print(msg.strip())
# print(msg.strip('#'))

# 填充（居中对齐，左对齐，右对齐）
# msg = '欢迎光临'
# print(msg.center(50, '*')) # 用*填充成50个字符，字符串居中对齐
# print(msg.ljust(50, '*'))  #左
# print(msg.rjust(50, '*'))  #右

# 练习
# ========================================
# 字符串处理，s = 'i,am,lili'
# 将分隔符','，修改成空格
# 取出最后一个单词lili
# 将上面字符串全部转换成大写
# s = 'i,am,lili'
# print(s.replace(',', ' '))
# print(s[5:])
# print(s.upper())
