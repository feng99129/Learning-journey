Ch2.变量和简单数据类型
2.2变量
 2.2.1变量的命名和使用
* 变量名只能包含字母，数字和下划线且不能以数字开头，也不能含有空格
* 不要将python关键字和函数名作为变量名
* 禁止使用小写字母l和大写字母O
2.3字符串
2.3.1修改字符串大小写
title() # 字符串中每个单词的首字母大写
upper() # 字符串中所有字母大写
lower() # 字符串中所有字母小写
代码示例:
name = "pink floyd"
print(name.title()) # name后面的'.'让python对变量name执行后面的title()指令，有些指令需要在括号中加入额外信息，此处title()括号中无需添加任何信息
output:
Pink Floyd
2.2.3在字符串中使用变量
利用f字符串的方法
代码示例：
first_name = "pink"
last_name = "floyd"
full_name = f"{first_name} {last_name}" # 第一个f字符串，将字符串内容中需要使用的变量用花括号括起来，打印时即可显示该变量指向的字符串
print(f"Hello,{full_name.title()}!") # 第二个f字符串，注意f字符串内非变量部分应放在花括号外
output:
Hello, Pink Floyd!
2.3.3使用制表符和换行符添加空白
制表符：\t
换行符：\n
代码示例:
print("Languages:\n\tPython\n\tC\n\tJavaScript")
output:
Languages:
	Python
	C
	JavaScript
2.3.4删除空白
删除字符串左端空白：lstrip()
删除字符串右端空白：rstrip()
删除字符串两端空白：strip()
代码示例：
favorite_language = " python "
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)
output:
 python 
python
2.4数
* 运算符号  
四则运算：'+','-','*','/'
乘方：'**'
* 任意两数相除结果总是浮点数，即便这两个数都是整数且能够整除
4/2
2.0
* 无论何种运算，只要操作中包含浮点数，python中的运算结果总是浮点数
* 数字中间加入下划线不改变其值，便于人们阅读很大的数字，但用带有下划线的数对变量进行赋值时，打印的结果中不会含有下划线
* 同时给多个变量赋值:
x, y, z = 0, 0, 0 # 进行该操作时应用逗号将变量名分开，且变量数目和数值数目要一一对应
* 常量：
python中没有内置的常量类型，通常将某个名称全为大写字母的变量视为常量



