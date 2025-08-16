print("Hello, World!")
"""
-----我是分割线-----
"""
print("\n\nend换行示例")
print("这样")
print("会在两行")
print("----------")
print("但是这样", end="")
print("会在一行")
"""
-----我是分割线-----
"""
print("\n\n保留关键字")
import keyword

print(keyword.kwlist)
"""
-----我是分割线-----
"""
print("\n\n多行注释")
"""
双引号多行注释
不会影响结果
"""
print("Hello, 双引号多行注释!")
'''
单引号多行注释
也不会影响结果
'''
print("Hello, 单引号多行注释!")
print("\n多行注释奇妙用法")
what = """
多行注释
不能这样用吧
人不能，至少不应该
"""
print(what)
"""
-----我是分割线-----
"""
print("\n\n缩进控制示例")
user_input = int(input("请输入一个大于5的数字，然后回车:"))
if user_input > 5:
    print("真棒，真听话")
else:
    print("不听话，坏")
