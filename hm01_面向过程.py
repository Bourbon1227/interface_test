"""
对象基础 - 编程方式【面向过程】
需求：
    把动物关冰箱，需要按照如下几步来进行操作
    1 把冰箱门打开
    2 把动物放进去
    3 把冰箱门关闭
"""

# 1 定义函数
def todo(animal):
    """案例函数"""
    if animal:
        print("1 把冰箱门打开")
        print("2 把{}放进去".format(animal))
        print("3 把冰箱门关闭")
    else:
        print("你倒是拉啊")

# 2 调用函数
todo("大象")
todo("")