s = input()

英文字符 = 0
数字 = 0
空格 = 0
其他字符 = 0

for char in s:
    # 仅统计英文字母（a-z、A-Z）
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        英文字符 += 1
    elif char.isdigit():  # 统计数字（0-9）
        数字 += 1
    elif char.isspace():  # 统计空格
        空格 += 1
    else:  # 其余归为其他字符
        其他字符 += 1

print(f"英文字符: {英文字符}")
print(f"数字: {数字}")
print(f"空格: {空格}")
print(f"其他字符: {其他字符}")
