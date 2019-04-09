# 变量和数据类型

a = 1
s = "hello python"
ss = r'today\n tomorrow'
sss = '''
ONE
TWO
THREE
'''

print(ss)
print(sss)
print(True and True)

# 常量，用大写字母表示

PI = 3.141592653

# 算术

print(9/3)
print(9//3)
print(9 % 3)

# 函数定义和调用


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(1.5))

# 空函数


def nop():
    pass

# 返回多个值，本质上是tuple
