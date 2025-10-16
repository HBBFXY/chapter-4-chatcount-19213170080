# 从键盘输入一行字符
s = input()

# 初始化各类字符计数器
英文字符 = 0
数字 = 0
空格 = 0
其他字符 = 0

# 遍历每个字符进行分类统计
for char in s:
    if char.isalpha():  # 判断是否为英文字母（含大小写）
        英文字符 += 1
    elif char.isdigit():  # 判断是否为数字
        数字 += 1
    elif char.isspace():  # 判断是否为空格
        空格 += 1
    else:  # 其余归为其他字符
        其他字符 += 1

# 按要求格式输出结果
print(f"英文字符: {英文字符}")
print(f"数字: {数字}")
print(f"空格: {空格}")
print(f"其他字符: {其他字符}")
