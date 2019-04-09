# 变量和数据类型
print("\n数据类型和变量相关：\n")

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
print("\n算术：\n")

print(9/3)
print(9//3)
print(9 % 3)

# 函数定义和调用
print("\n函数相关：\n")


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


def double(x, y):
    return x*2, y*2


x2, y2 = double(2, 4)  # 类似JS的解构
print(x2, y2)

print(double(2, 4))

# 默认参数值


def default(x=2):
    return x*2


print(default())


# 可变参数，两种方案：1. 利用tuple或者list；2. 使用*标记符（tuple）

def flexible(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print(flexible(1, 2, 3, 4))

# 关键字参数，注意：关键字参数得到的是一份（dict）拷贝


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 命名关键字参数，传参时需要传入参数名


def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('Jack', 24, city='Beijing', job='Engineer')

# 参数组合。在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 高级特性
print("\n高级特性：\n")

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[-1])
print(L[:])  # 拷贝
print(list(range(10)))  # range操作

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
